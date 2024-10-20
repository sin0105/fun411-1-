#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab10_2
# 204111 Sec 003
# TA 66-Film

def main():
    test()

def longest_digit_run(n: int):
    n = str(n)+'.'              # เติมจุดตอนท้ายเนื่องจาก ตัวโค้ดจะเก็บค่าเมื่อตัวถัดไป != ตัวด้านหน้า
    index = 0
    new = 0
    num = n[0]                  #  ตัวเร่ิมในการไล่เช็ค index
    all_list = []

    while index < len(n):       # หยุดทำงานเมื่อค่า index >= len(n)
        if num == n[index]:     # หาก index เหมือนกันให้ 
            new += 1                # new +1 ไปเรื่อยๆ เพราะต้องการนับจำนวน (1111 => 4)
            index += 1              # index เพิ่มค่าไปเรื่อยๆ แต่ไม่เกิน len(n)
        else:
            all_list.append(new)      # ให้[all_list] เก็บรวบรวม (677 new => [1, 2])
            num = n[index]      # เปลี่ยนจากการเริ่ม (num[0] => num[index]) เพราะต้องส่ง num เป็น index ที่มีการเปลี่ยนแปลง
            new = 1             # เปลี่ยนจากการเริ่ม (new = 0 => new =1)
            index += 1
    return max(all_list)

def test():
    assert longest_digit_run(117773333) == 4
    assert longest_digit_run(11777332) == 3
    assert longest_digit_run(1177332) == 2
    assert longest_digit_run(12121212121212121212121212121) == 1
    print("SA TUUUU 99")


if __name__ == '__main__':
    main()
