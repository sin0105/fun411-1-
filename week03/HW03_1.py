#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW03_1
# 204111 Sec 003
import math
def main():
    test_nearest_odd()
   


# implement ฟังก์ชันนี้ให้ถูกต้อง
def nearest_odd(x: float) -> int:
    odd_num = ((math.ceil(x/2))*2)-1   # นำค่าที่รับมา/2 จากนั้นปัดเศษขึ้นเพื่อนทำเป็นจำนวนเต็ม นำไปคูณด้วย2จากนั้นลบ1
    return odd_num


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_nearest_odd() -> None:
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("All OK!")


if __name__ == '__main__':
    main()