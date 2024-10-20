#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab12_1
# 204111 Sec 003
# TA 66-Film

def main():
    display_calendar(6, 2005)


def display_calendar(month: int, year: int):
                                            # หาจำนวนวันจากเดือน
    if month in [1, 3, 5, 7, 8, 10, 12]: 
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:                        # หากเป็น leap year ให้เดือนที่ 2 บวกเพิ่ม 1 วัน
        if (year % 400 == 0): plus =  1
        elif (year % 100 == 0): plus =  0
        elif (year % 4 == 0): plus =  1
        else: plus =  0 
        max_day = 28 + plus

    if month in [1,2]:                      # leap year มีผลต่อ เดือน 1,2 
        year -= 1                               # ให้ใช้เป็นเดือน 13,14 และให้ปีลดลง 1
        month += 12


    list_day_tail = list(map(lambda x: str(x).zfill(2),range(1,max_day+1)))         # _1 _2 _3 ... _9
    list_day_head = list(map(lambda x: x.replace('0',' '),list_day_tail[:9]))       # 10 11 ... max_day
    all_list_day = list_day_head + list_day_tail[9:] 

    index_day = (((1 + ((13*(month+1))//5) + year%100 + ((year%100)//4) +\          # สูตรการหาว่าวันที่ 1 คือวันอะไร
                (year//100)//4 - 2*(year//100))%7+5) %7)+1
    if index_day == 7:
        index_day = 0
    
    print('Su Mo Tu We Th Fr Sa')
    print('-- '*index_day, end='') 
    roundd = index_day             # ให้เก็บ roundd เริ่มต้นที่ index_day
    for num in all_list_day: 
        roundd += 1
        print(num, end=' ')        # print num ไปเรื่อยๆ และให้ roundd เพิ่มทีละ 1
        if roundd == 7:            # roundd เป็น 7 ให้ enter และเริ่ม roundd ใหม่
            print()
            roundd = 0
    print('\n')


if __name__ == '__main__':
    main()