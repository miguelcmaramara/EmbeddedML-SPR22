

def sub_avg(lst, num_data):
    if num_data == 0:
        return lst
    sum = 0
    res = []

    for i in range(num_data):
        sum += lst[i]
    
    avg = sum / num_data
    print("avg: ", avg)
    
    for num in lst:
        print(num, "   ", avg)
        res.append(num - avg)
    
    return res


def sub_avg_all(lsts, num_data):
    res = []
    for lst in lsts:
        res.append(sub_avg(lst, num_data))
    
    print("-----")
    return res


def apply_to_all(fxn, lsts):
    # applies a specific function to all lists in the list
    res = []
    for lst in lsts:
        res.append(fxn(lst))
    
    return res


def all_to_all(fxns, lsts):
    # applies every function in a list of functions to every list in a list of lists
    res = []
    for lst in lsts:
        for fxn in fxns:
            lst = fxn(lst)
        res.append(lst)
    return res
        


def correct_units(lst, cf):
    # Multiplies a correction factor by mutiplying each element by it
    res = []
    for num in lst:
        res.append(num*cf)

    return res


def averaging_filter(lst, num_avg, trailing=False):
    if num_avg < 1: return lst

    # replaces the i'th value in a list with a runnin average between it and the next
    # few (specified by num_avg) items in the list
    # Trailing means that it will make smaller avaerages as it runs out of space.
    #   for example, if you average 30 together, the 15th to last value will only average 14 together

    for i, val in enumerate(lst):
        if(i <= len(lst) - num_avg):
            lst[i] = sum(lst[i:i+num_avg])/num_avg
        elif(trailing):
            lst[i] = sum(lst[i:])/(len(lst) - i)

    return lst

def low_pass_filter(lst, threshold, center_only=False):
    # Replaces a number with the previous if the difference between is too small
    # center only only apply this rule when the close to zero

    if threshold == 0: return lst

    res = []
    if center_only:
        for val in lst:
            if(val < threshold and val > -threshold):
                res.append(0)
            else:
                res.append(val)
        return res
    
    if not center_only:
        for i in range(len(lst)):
            if( i > 0 and lst[i] < res[i-1] + threshold and lst[i] > res[i -1] - threshold):
                res.append(res[i-1])
            else:
                res.append(lst[i])
        return res


def append_numbers(lst, num_of_nums, num_to_append=0,  stretch=False):
    # appends a bunch of numbers to a list
    # for example, given lst x = [0,1,2,4,6],  num_of_nums = 4, num_to_append = 5,
    # the following is returned:[0,1,2,4,6, 5, 5, 5, 5]
    
    # Stretch means that the array would take the average difference in units and append that difference
    # rendering num_to_append meaningless

    if(stretch):
        cumm_diff = 0
        for i in range(len(lst ) - 1):
            cumm_diff = cumm_diff + (lst[i + 1] - lst[i])
        
        avg_diff = cumm_diff / (len(lst) - 1)

        for i in range(num_of_nums):
            lst.append(lst[len(lst) - 1] + avg_diff)

        return lst

    return lst + ([num_to_append] * num_of_nums)
    


if __name__ == "__main__":
    # Testing code
    # print(averaging_filter([0,2,4,8,16],2))
    # print(low_pass_filter([0,2,4,8,16], 5, False))
    # print(append_numbers([0,2,4,8,16], 5, 4))
    print(append_numbers([0,2,4,6,8], 4, stretch=True))
