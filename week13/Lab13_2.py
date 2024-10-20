#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab13_2
# 204111 Sec 003

def main():
    dis = [[2, 3, 4], [1, 2]]
    square_matrix(dis)
    print(dis)
    # print(square_matrix([[1, 2], [1, 2, 3], [1, 2], [1, 2], [1]]))
    # print(square_matrix([[0], [1, 2,3]]))

def square_matrix(list_x: list[list[int]]):
    colm = max(list(map(lambda x: len(x), list_x)))
    row = len(list_x)
    all_max = max([colm, row])

    minus = []
    for i in list_x:
        if all_max - len(i) >= 0:
            minus.append((all_max - len(i)))

    solute1 = []
    for i in minus:
        solute1 += [[0]*i]
  
    solute2 = []
    for i in range(row):
        solute2.append(list_x[i] + solute1[i])

    solute3 = []
    if colm > row:
        for i in range(colm-row):
            solute3 += [[0]*colm]
    list_x[:] = solute2 + solute3
    

if __name__ == '__main__':
    main()
    # assert (square_matrix([[2, 3, 4], [1, 2, 3]])) == [[2, 3, 4],[1, 2, 3],[0, 0, 0]]
    # assert (square_matrix([[1, 2], [1, 2, 3], [1, 2], [1, 2], [1]])) == [[1, 2, 0, 0, 0],[1, 2, 3, 0, 0],[1, 2, 0, 0, 0],[1, 2, 0, 0, 0],[1, 0, 0, 0, 0]]
    # assert (square_matrix([[1, 2], [3, 4], [5, 6]])) == [[1,2,0],[3,4,0],[5,6,0]]
    # assert (square_matrix([[1,2,3], [1,2,3], [1,2,3]])) == [[1,2,3], [1,2,3], [1,2,3]]
    # print('k')
