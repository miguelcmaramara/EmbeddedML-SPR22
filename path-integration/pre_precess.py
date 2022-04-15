
def sub_avg(lst, num_data):
    if num_data == 0: return lst
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


def correct_units(lst, cf):
    res = []
    for num in lst:
        res.append(num*cf)

    return res


def apply_to_all(fxn, lsts):
    res = []
    for lst in lsts:
        res.append(fxn(lst))
    
    return res
