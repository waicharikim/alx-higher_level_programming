#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_num = 0
    total_den = 0
    for i in my_list:
        total_num += int(i[0] * i[1])
        total_den += i[1]
    return total_num/total_den
