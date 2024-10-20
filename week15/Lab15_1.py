#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab15_1
# 204111 Sec 003

def main():
    assert sum_nested_list([1, 2, [[3, [[4], 5]], [6, 7]]]) == 91
    assert sum_nested_list([1, [2, [3]]] ) == 14
    assert sum_nested_list([1, [[2, [3]], 4, [5]], [6, [7]]]) == 75
    assert sum_nested_list([9, [[8, [7]], 6, [5, [44, [33]]]]] ) == 429
    assert sum_nested_list([1, 2, [[3, 0], 4], 8]) == 28
    print('yung ngai ko dai la')
    

def sum_nested_list(list_a: list,roundd = 1):
    result = 0
    for i in list_a:
        if type(i) == int:
            result += (i*roundd)
        else:
            result += sum_nested_list(i,roundd+1)
    return result



if __name__ == '__main__':
    main()