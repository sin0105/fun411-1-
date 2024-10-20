#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW12_3
# 204111 Sec 003
# TA 66-Film TA 67-Tan

DEBUG = False
import random
import time
def main():
    assert ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]) == \
        {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}
    print("ja dai pai aan kme leaw")


def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    # สูตรระเบิด 9 ช่อง
    plus = set([(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, 0), (0, -1), (1, 1), (1, 0), (1, -1)]) 

    bomb_list = set(bomb_list) # แปลง bomb_list เป็น set
    dictionary = dict()
    for i in bomb_list:
        for j in plus:

            # ขอบเขตของระเบิด และไม่นับระเบิดที่เป็นตัวมันเอง
            if (i[0]+j[0]) != -1 and (i[0]+j[0]) != m and (i[1]+j[1]) != -1 and (i[1]+j[1]) != n  \
                and (i[0]+j[0], i[1]+j[1]) not in bomb_list:
                dictionary[(i[0]+j[0], i[1]+j[1])] = 1 + dictionary.get((i[0]+j[0], i[1]+j[1]),0)
                #_______( ex ) dictionary[(1, 1)] = 1 + dictionary.get((1, 1), 0) ---> {(1, 1): 5}
                
            continue
    return dictionary
    if DEBUG: print('dictionary ',dictionary)
   
def print_board(n_row, n_col, b_list):
    max_len = len(str(max(n_row, n_col)))
    pad = ' '
    board_str = []
    board_str += [pad + pad*(max_len) +
                  pad.join(map(lambda x: str(x).zfill(max_len), range(n_col)))]

    for i in range(n_row):
        for j in range(n_col):
            if j == 0:
                temp = str(i).zfill(max_len) + pad
            pad2 = ' ' * (max_len - 1)
            if (i, j) in b_list:
                temp += pad2 + 'B' + pad
            else:
                temp += pad2 + '.' + pad
        board_str += [temp.rstrip()]

    print('\n'.join(board_str))


if __name__ == '__main__':
    main()    