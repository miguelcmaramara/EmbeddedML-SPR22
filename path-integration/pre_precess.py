
def sub_avg(lst, num_data):
    if num_data == 0: return lst
    sum = 0
    res = []

    for i in range(num_data):
        sum += lst[i]
    
    avg = sum / num_data
    
    for num in lst:
        res.append(num - avg)
    
    return res


def sub_avg_all(lsts, num_data):
    res = []
    for lst in lsts:
        res.append(sub_avg(lst, num_data))
    
    print("-----")
    return res
