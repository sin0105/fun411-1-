#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW04_3
# 204111 Sec 003
# TA Film

def main():
    test_rectangle()
   
    
def is_overlapped(l1: float, t1: float, w1: float, h1: float,
                  l2: float, t2: float, w2: float, h2: float) -> bool:  

    if ((l1+w1)-(l2)<0) or ((l2+w2)-(l1)<0) or ((t1+h1)-(t2)<0) or ((t2+h2)-(t1)<0):  
        return False
    else :
        return True


def test_rectangle():
    assert is_overlapped(10,10,100,150,50,100,150,200) == True
    assert is_overlapped(10,10,90,90,150,90,50,90) == False
    print("All OK")
    

if __name__ == "__main__":
    main()

# มองให้ดป็นเส้น เส้น l1+w เอาไปเทียบด้วย l2 ทำซ้ำ 4 มุม
# นำค่าที่ได้ไปเทียบกับ 0 
# ถ้าน้อยกว่่า 0 กำหนดให้ สี่เหลี่ยมทั้ง 2 รูปไม่ทับซ้อนกัน คืนค่าเป็น False
# ถ้ามากกว่่า 0 กำหนดให้ สี่เหลี่ยมทั้ง 2 รูปทับซ้อนกัน คืนค่าเป็น True
# ใช้ตัวดำเนินการ or