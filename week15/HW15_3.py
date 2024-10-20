#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Hw15_3
# 204111 Sec 003

def main():
    print(count_segment([(2, 7, 1.5), 
                       (3.2, 2.5, 4.06), 
                       (-5.5, -4.5, 2.5), 
                       (2, -5.2, 3), 
                       (7.2, -2.8, 1.2)]))

    # count_segment([(2, 7, 1.5)])
    # count_segment([(3.2, 2.5, 4.06)])
    # count_segment([(-5.5, -4.5, 2.5)])
    # count_segment([(2, -5.2, 3)])
    # count_segment([(7.2, -2.8, 1.2)])
    # count_segment([(2,0,8)])

def count_segment(list_a: list[tuple[float]]):
    dic = dict(q1 = 0, q2 = 0, q3 = 0, q4 = 0)
    for i in list_a:
        if i[0] > 0  and i[1]> 0:
            dic['q1'] += 1
            if i[0] < i[2]:
                dic['q2'] += 1
            if i[1] < i[2]:
                dic['q4'] += 1
            if ((i[0]**2) + (i[1]**2))** 0.5 < i[2]:
                dic['q3'] += 1

        elif i[0] < 0  and i[1] > 0:
            dic['q2'] += 1
            if abs(i[0]) < i[2]:
                dic['q1'] += 1
            if i[1] < i[2]:
                dic['q3'] += 1
            if ((abs(i[0])**2) + (i[1]**2))** 0.5 < i[2]:
                dic['q4'] += 1

        elif i[0] < 0  and i[1] < 0:
            dic['q3'] += 1
            if abs(i[0]) < i[2]:
                dic['q4'] += 1
            if abs(i[1]) < i[2]:
                dic['q2'] += 1
            if ((abs(i[0])**2) + (abs(i[1])**2))** 0.5 < i[2]:
                dic['q1'] += 1

        elif i[0] > 0  and i[1] < 0:
            dic['q4'] += 1
            if i[0] < i[2]:
                dic['q3'] += 1
            if abs(i[1]) < i[2]:
                dic['q1'] += 1
            if ((i[0]**2) + (abs(i[1])**2))** 0.5 < i[2]:
                dic['q2'] += 1




        elif i[0] == 0  and i[1] > 0:
            dic['q1'] += 1
            dic['q2'] += 1
            if i[2] > i[1]:
                result  += (3, 4)
                dic['q3'] += 1
                dic['q4'] += 1

        elif i[0] == 0  and i[1] < 0:
            dic['q3'] += 1
            dic['q4'] += 1
            if i[2] > abs(i[1]):
                dic['q1'] += 1
                dic['q2'] += 1

        elif i[0] > 0  and i[1] == 0:
            dic['q1'] += 1
            dic['q4'] += 1
            if i[2] > i[0]:
                dic['q2'] += 1
                dic['q3'] += 1

        elif i[0] < 0  and i[1] == 0:
            dic['q2'] += 1
            dic['q3'] += 1
            if i[2] > abs(i[0]):
                dic['q1'] += 1
                dic['q4'] += 1

        elif i[0] == 0  and i[1] == 0:
            dic['q1'] += 1
            dic['q2'] += 1
            dic['q3'] += 1
            dic['q4'] += 1

    return tuple(dic.values())


if __name__ == '__main__':
    main()