#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW10_1
# 204111 Sec 003
# TA 66-Film

def main():
    result = eratosthenes(121,True)
    print('----')
    print(result)


def eratosthenes(n: int, show_step: bool=False):
    prime = list(range(2,n+1))    # คิดตั้งแต่ 2 เป็นต้นไป เนื่องจาก 1 ไม่เป็นจำนวนเฉพาะ
    po = 2
    
    while po <= n**0.5:         # จำกัดเขต ตามนิยามจำนวนเฉพาะ 
        if po in prime:           # คิดเฉพาะ position ที่อยู่ใน prime เท่านั้น => (4 not in prime [2,3,5,7])
            prime = list(filter(lambda x: x % po != 0 or x == po,prime))  # กรองตัวที่หาร po ลงตวออก เก็บ prime ที่เท่ากับ po ไว้
            if show_step == True:
                print(str(po)+':',prime)
        po += 1
    return prime


if __name__ == '__main__':
    main()