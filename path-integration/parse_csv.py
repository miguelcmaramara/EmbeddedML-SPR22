import csv

# Reads in the values inbetween the Begin and exit statements and returns a tuple of values
def read_event_BEGIN_TO_EXIT(x_list,y_list,z_list,time_list, get_from_csv):
    send_event = []
    xout = []
    yout = []
    zout = []
    tout = []
    for i in range(0, len(get_from_csv)-1):
        if "BEGIN" in str(time_list[i]):
            # send_event = []
            j = i + 1
            while "EXIT" not in str(time_list[j]):
                send_event.append([x_list[j], y_list[j], z_list[j], time_list[j]])
                xout.append(x_list[j])
                yout.append(y_list[j])
                zout.append(z_list[j])
                tout.append(time_list[j])

                j += 1
                # print(time_list[j])
            return (xout, yout, zout, tout)

def csv_to_list(filePath):

    # Step 1: Reads the CSV file and inputs values into get_from_csv list
    file = open(filePath, "r")
    csv_reader = csv.reader(file)

    get_from_csv = []
    count = 0
    for row in csv_reader:
        if("BEGIN" in row[0]):
            count += 1
        get_from_csv.append(row)

    print(count)

    # Step 2: Creates lists to record time, x, y, z values in lists individually
    time_list = []
    x_list = []
    y_list = []
    z_list = []

    # Step 3: Input values for each list from each column
    for row in get_from_csv:
        if len(row) <= 3:
            correct_time = row[0].split()
            time_list.append(correct_time[len(correct_time)-1])
            x_list.append(float(row[1]))
            y_list.append(float(0))
            z_list.append(float(0))

        if len(row) > 3:
            correct_time = row[0].split()
            time_list.append(int(correct_time[len(correct_time) - 1]))
            x_list.append(float(row[1]))
            y_list.append(float(row[2]))
            z_list.append(float(row[3]))

    # Step 4: Creates master_list, a tuple of all lists recorded
    addList = []
    for i in range(0, len(get_from_csv)):
        if "BEGIN" not in str(time_list[i]) and "EXIT" not in str(time_list[i]):
            addList.append([time_list[i], x_list[i], y_list[i], z_list[i]])

        # print(str(time_list[i]) + ", " + str(x_list[i]) + ", " + str(y_list[i]) + ", " + str(z_list[i]))
    master_list = (x_list, y_list, z_list, time_list)

    print(master_list)

    print(read_event_BEGIN_TO_EXIT(x_list, y_list, z_list, time_list, get_from_csv))
    return(read_event_BEGIN_TO_EXIT(x_list, y_list, z_list, time_list, get_from_csv))



if __name__ == '__main__':
    csv_to_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
