#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW09_2
# 204111 Sec 003

def main():
    left_max([2,1,8,4])


def left_max(list_a: list[int]):
    new = list(map(lambda x: sorted(list_a[:x]),range(1,len(list_a)+1)))   # [2] , [1,2] , [1,2,8] 
    front = list(map(lambda x: new[x][-1],range(0,len(list_a)-1)))         # [2, 2, 8]
    back = [max(list_a)]                                                   # [8]
    result = front + back                                                  # [2, 2, 8, 8]
    print(result)
    return result


if __name__ == '__main__':
    main()