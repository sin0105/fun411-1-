#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab04_1
# 204111 Sec 003


# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()
from math import isclose

def main():
    test_circle_intersect()
    


def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon=10**-6):
    distance = (((x1-x2)**2)+((y1-y2)**2))**0.5   # สูตรการหาระยะห่างระหว่างจุด 2 จุด
    if isclose(distance,r1+r2,abs_tol=epsilon) :  # (ค่า1,ค่า2,เท่ากับ) ค่า1 - ค่า2 = (ไม่เกินค่า epsilon)
        return 0
    elif (r1+r2)-distance < 0:                    # ถ้าได้ค่าน้อยกว่า 0 หมายความว่าวงกลมทั้ง 2 ทับซ้อนกัน
        return -1
    elif (r1+r2)-distance > 0:                    # ถ้าได้ค่ามากกว่า 0 หมายความว่าวงกลมทั้ง 2 ไม่ทับซ้อนกัน
        return 1

def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()
