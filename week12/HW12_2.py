#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW12_2
# 204111 Sec 003
# TA 66-Film

import sys

def main():
    treasures = read_input()
    assert total_value('Gold', treasures) == 1090
    assert total_value('Ruby', treasures) == -1
    print('non dia leaw')


def read_input():
    treasures = {}
    for line in sys.stdin: # อ่านไฟล์ python3 HW12_2 < input.txt
        if '#' in line:
            continue
        line = line.split(', ')     # ( 1 )[Marineford, Platinum, 42000]
        if line[1] in treasures:    # สมบัติ อยู่ใน dic ซ้ำ
            treasures[line[1]] += [(line[0], int(line[2].replace('\n','')))]    # int(เอาเงินเพิ่ม เอา\n ออก)
        else:
            treasures[line[1]] = [(line[0],int(line[2].replace('\n','')))]      # int(เก็บค่าเงิน เอา\n ออก)
    return treasures
    '''
    {'Platinum': [('Marineford', 42000)], 
    'Diamond': [('Marineford', 300)], 
    'Bronze': [('Enies Lobby', 43000)], 
    'Silver': [('Elbaf', 9600)], 
    'Gold': [('Dressrosa', 190), ('Punk Hazard', 900)]}
    '''


def total_value(treasure_type, treasures):
    if treasure_type not in treasures.keys(): # ถ้าหาสมบัตไม่เจอ คืนค่า -1
        total = -1
    else:
        total = sum(list(map(lambda x: treasures[treasure_type][x][1],range(len(treasures[treasure_type])))))
    return total


if __name__ == '__main__':
    main()






