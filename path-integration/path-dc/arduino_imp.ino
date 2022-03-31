/**
 * Libraries and outside files
 */
#include <Arduino_LSM9DS1.h>



unsigned int numData = 0;
const unsigned int INPUT_LENGTH = 1000;
const unsigned int SWITCH_PIN = 2;
unsigned long t = 0;
float xIn [INPUT_LENGTH]; //Takes from IMU
float yIn [INPUT_LENGTH];
float zIn [INPUT_LENGTH];
float tIn [INPUT_LENGTH];
float gx [INPUT_LENGTH]; //gyroscope data from IMU
float gy [INPUT_LENGTH];
float gz [INPUT_LENGTH];
int delayTime = 10;

int i;
/*****************************************
 * SETUP
 ****************************************/
void setup() {
  // don't miss serial output
  Serial.begin(9600);

  pinMode(SWITCH_PIN, INPUT);

  // Begin IMU
  if(!IMU.begin()){
    Serial.print("IMU failed to initialize");
  }

}

void loop() {
  if(digitalRead(SWITCH_PIN) == HIGH && IMU.accelerationAvailable() && IMU.gyroscopeAvailable()){
    Serial.println("in switch loop");
    t = millis();
    numData = 0;
    while(digitalRead(SWITCH_PIN) == HIGH && numData < INPUT_LENGTH){
      //Data collection
      IMU.readAcceleration(xIn[numData],yIn[numData],zIn[numData]);
      IMU.readGyroscope(gx[numData], gy[numData], gz[numData]);

      //prints out x, y, z, values in each row due to Serial.print() function constraints
      Serial.print(millis() - t);
      Serial.print(", ");
      Serial.print(xIn[numData], 5);
      Serial.print(", ");
      Serial.print(yIn[numData], 5);
      Serial.print(", ");
      Serial.print(zIn[numData], 5);
      Serial.print(", ");
      Serial.print(gx[numData], 5);
      Serial.print(", ");
      Serial.print(gy[numData], 5);
      Serial.print(", ");
      Serial.println(gz[numData], 5);
      
      tIn[numData] = (float) (millis()-t);

      numData++;
      delay(delayTime);
      
    }

  }
  delay(delayTime);

}





/**
 * 
 *  Linear interpolation functions
 *  
 */





void printArr(String label, float arr[], unsigned int arrSize ){
  Serial.println(label);
  
  Serial.print("[ ");
  for(int i = 0; i < arrSize; i++){


    Serial.print(arr[i],5);
    if(i != arrSize - 1) Serial.print(", ");

  }
  Serial.println("]");
  /*
  for(int i = 0; i < arrSize/2; i++){
    Serial.print(i);
    Serial.print(": ");
    Serial.print(arr[i],5);
    Serial.print("        ");
    Serial.print(i + arrSize/2);
    Serial.print(": ");
    Serial.println(arr[i+arrSize/2],5);
  }
*/
  Serial.println("done\n\n");
}
