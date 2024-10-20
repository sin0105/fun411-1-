#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW13_3
# 204111 Sec 003
# TA-67 Toey

def main():
    print(sum_d_product([[3, 3, 3, 2], [2, 0, 3, 1], [2, 1, 2, 3], [1, 0, 2, -1]]))
    print(sum_d_product([[1, 1, 5, -1], [12, 2, -2, 0], [4, 8, 8, 12], [4, 12, 12, 15]]))
    print(sum_d_product([[0, -1, -1, 3, 2, 3, -1, 3], [3, -1, -1, 2, 0, -1, 2, 1], [3, 0, 1, 2, 3, 1, 3, 1], [2, 2, 1, -1, -1, 2, 0, 3], [1, 3, 2, 1, 3, 2, 2, 1], [1, 2, 2, 1, 3, 3, 1, 3], [2, 2, 2, 2, 2, 2, 3, 3], [1, 3, 2, 3, 1, 1, 2, 2]]))
    

def sum_d_product(m: list[list[int]]):
    if len(m) == 2:
        return (m[0][0]*m[1][1]) + (m[0][1]*m[1][0])

    ans = []
    for i in range(0,len(m),2): 
        skip1 = range(0,len(m[0]),2)
        skip2 = range(1,len(m[0]),2)
        solution = list(map(lambda x,y : (m[i][x] * m[i+1][y]) + (m[i][y] * m[i+1][x]),skip1, skip2))
        ans.extend([solution])

    result = sum_d_product(ans)
    return result

if __name__ == '__main__':
    main()