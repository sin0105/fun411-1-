#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab04_2
# 204111 Sec 003

def main():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    c = int(input("Input c: "))
    my_min_mid_max(a,b,c)


def my_min_mid_max(a: int, b: int, c: int):
    if (a>=b) and (b>=c):                        
        maxx = a            
        midd = b
        minn = c
    elif (a>=c) and (c>=b):
        maxx = a 
        midd = c
        minn = b
    elif (b>=a) and (a>=c):
        maxx = b
        midd = a
        minn = c
    elif (b>=c) and (c>=a):
        maxx = b
        midd = c
        minn = a
    elif (c>=a) and (a>=b):
        maxx = c
        midd = a
        minn = b
    else :
        maxx = c
        midd = b
        minn = a
    print ("min =",minn,"\nmid =",midd,"\nmax =",maxx)


if __name__ == '__main__':
    main()

# วิธีนี้ไม่ค่อยดีฮะ ดีที่สุดคือ if 3 ตัว สั้นกระชับเข้าใจง่ายกว่า
# คิดความน่าจะเป็นของข้อมูล 3! = 6 มีทั้งหมด 6 กรณีคิดให้หมด