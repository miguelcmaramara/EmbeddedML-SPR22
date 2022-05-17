from parse_csv import csv_to_list
import matplotlib.pyplot as plt
import tensorflow
from keras.datasets import mnist
import numpy as np
from keras.models import load_model
from scipy.interpolate import interp1d
print("Loading raw csv data")
tuple_of_lists = csv_to_list("C:/Users/jaden/OneDrive/Desktop/HomeWork/VIP/EmbeddedML-SPR22/path-integration/path-raw-csv/numbers.csv")[0]

print("Loading handwriting OCR model")
model = load_model("path-model/mnist.h5")

# To Do
# 1. Plot data from numbers.csv
# 2. Save plot as image and/or array
# 3. Run model prediction on image to classify character
ac_x = tuple_of_lists[0]
ac_y = tuple_of_lists[1]
ac_z = tuple_of_lists[2]
time = tuple_of_lists[3]

gx = tuple_of_lists[4]
gy = tuple_of_lists[5]
gz = tuple_of_lists[6]


print("Length " + str(len(gx)))
x = np.linspace(0, 28, len(ac_x))
f_acx = interp1d(x, ac_x)
f_acy = interp1d(x, ac_y)
f_acz = interp1d(x, ac_z)

f_gx = interp1d(x, gx)
f_gy = interp1d(x, gy)
f_gz = interp1d(x, gz)

#Create a new sample set with the desired sample size by rescaling
#the original one
xnew = np.linspace(0, 28, 50)
acx_stretch = f_acx(xnew)
acy_stretch = f_acy(xnew)
acz_stretch = f_acz(xnew)

gx_stretch = f_gx(xnew)
gy_stretch = f_gy(xnew)
gz_stretch = f_gz(xnew)

linearized_vals = np.concatenate((acx_stretch, acy_stretch, acz_stretch, gx_stretch, gy_stretch, gz_stretch))
linearized_vals.resize(1, 28,28, 1)
linearized_vals.reshape(1,28,28,1)
linearized_vals /= 255
#plt.plot(linearized_vals)
#plt.show()

predictions = model.predict(linearized_vals)[0]

print("\nResults")
print("_____________________")
print("Prediction: ")
print(np.argmax(predictions))
print("Accuracy: " )
print(max(predictions)*100)






