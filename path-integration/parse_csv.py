import csv


# Reads in the values inbetween the Begin and exit statements and returns a tuple of values
def read_event_BEGIN_TO_EXIT(x_list,y_list,z_list,time_list, get_from_csv, start):
    send_event = []
    x_set_list = []
    y_set_list = []
    z_set_list = []
    time_set_list = []
    for i in range(start, len(get_from_csv)):
        if "BEGIN" in str(time_list[i]):
            # send_event = []
            j = i + 1
            while "EXIT" not in str(time_list[j]):
                x_set_list.append(x_list[j])
                y_set_list.append(y_list[j])
                z_set_list.append(z_list[j])
                time_set_list.append(time_list[j])
                # send_event.append([x_list[j], y_list[j], z_list[j], time_list[j]])
                j += 1
                # print(time_list[j])
            send_event = [x_set_list, y_set_list, z_set_list, time_set_list]
            return tuple(send_event)

def csv_to_list(path_name):

    # Step 1: Reads the CSV file and inputs values into get_from_csv list
    file = open(path_name, "r")
    csv_reader = csv.reader(file)

    get_from_csv = []
    index_of_start_statements = []
    count = 0
    index = 0
    for row in csv_reader:
        if("BEGIN" in row[0]):
            index_of_start_statements.append(index)
            count += 1
        index += 1
        get_from_csv.append(row)

    print(count)
    print(index_of_start_statements)

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

    final_list = []
    for i in range(0, len(index_of_start_statements)):
        value = read_event_BEGIN_TO_EXIT(x_list, y_list, z_list, time_list, get_from_csv, index_of_start_statements[i])
        #print(value)
        final_list.append(value)


    print(final_list)
    return final_list


if __name__ == '__main__':
    csv_to_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
