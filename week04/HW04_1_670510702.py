#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW04_1
# 204111 Sec 003

def main():
    print(calculate_exp(20,20))
    test_exp()
   
def calculate_exp(p: int, c: int):
    round_exp = (((p+c)-13)//11)+1   
    exp = round_exp*1000       
    if p == 0:                      # เมื่อไม่มีนกเป็นตัวตั้งต้นจะไม่สามารถคำนวนหา exp ได้เลย ไม่ว่าจะมีลูกอมมากแค่ไหน
        exp = 0
    if round_exp > p:               # แม้ว่าจะได้จำนวนรอบมากกว่านกเท่าไหร่ ให้ยึดจำนวนนกเป็นหลัก
        exp = p*1000

    return exp

def test_exp():
    assert calculate_exp(5,55) == 5000
    assert calculate_exp(0,32) == 0
    assert calculate_exp(55,5) == 5000
    assert calculate_exp(1200,0) == 108000
    assert calculate_exp(11,12) == 1000
    assert calculate_exp(2,12) == 1000
    assert calculate_exp(1,12) == 1000
    assert calculate_exp(2,22) == 2000
    assert calculate_exp(2,100) == 2000

    print("All OK")
    

if __name__ == "__main__":
    main()

'''
13 ได้จาก นก1+ลูกอม12 
11 ได้จาก 13-2 
-2 คือนกที่ evo และลูกอมที่ได้หลังการevo 
//11 เป็นการหาจำนวนรอบ การทำซ้ำแบบมีรูปแบบ 
11 เป็นรูปแบบจริงแต่ในตอนแรกคือการ -13 
แสดงว่ารอบการทำงานจริง = รอบเดิน+1
ค่าที่ได้คือ จำนวนรอบนำไป * 1000 เพื่อหา exp
แต่ ^ ไปอ่านข้างบน
'''