#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW09_2
# 204111 Sec 003
"""
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]                                      ->(20//3 = 6) 1 ช่วงมี 6
a = [1,2,3,4,5,6]       b = [7,8,9,10,11,12]       c = [13,14,15,16,17,18,19,20]          ->(6//3 = 2) 1 ช่วงมี 2, (8//3 = 2)
a = [1,2] [3,4] [5,6]   b = [7,8] [9,10] [11,12]   c = [13,14] [15,16] [17,18,19,20]      ->(4//3 = 1) 1 ช่วงมี 1, return มี 2 นำไป sum/2
a = [1.5] [3.5] [5.5]   b = [7.5] [9.5] [11.5]     c = [13.5] [15.5] [[17] [18] [19,20]]  ->(4//3 = 1), return มี 1 ส่ง ,return มี 3 ดึง mid ออกมา            
a = [3.5]               b = [9.5]                  c = [17, 18, 19.5]                                    
                                                   c = [18]
return median_of_median([a,b,c]) -> ส่งไป recursion

"""

def main():
    print(median_of_median([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))


def  median_of_median(list_a: list[float]):
    if len(list_a) == 1:
        return list_a[0]
    if len(list_a) == 2:   
        return (sum(list_a))/2
    if len(list_a) == 3:
        if list_a.count(max(list_a)) >= 2:
            list_a = max(list_a)
        elif list_a.count(min(list_a)) >= 2:
            list_a = min(list_a)
        else:
            list_a = list(filter(lambda x: x != max(list_a) and x != min(list_a),list_a))
            list_a = list_a[0]
        return list_a

    lenny = len(list_a)//3
    r1 = list_a[:lenny]
    r2 = list_a[lenny:lenny*2]
    r3 = list_a[lenny*2:]

    row1 = median_of_median(r1)
    row2 = median_of_median(r2)
    row3 = median_of_median(r3)
    
    return median_of_median([row1,row2,row3])

if __name__ == '__main__':
    main()


