#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab06_1
# 204111 Sec 003

def main():
    test_triangle()


def triangle(n):
    rangee = list(range(2,n))                                        # คิด .... เริ่มจากแถวที่ 2 ถึง แถวก่อนสุดท้าย
    immage = list(map(lambda m: '*'+'.'*(2*m-3)+'*',rangee))         # จะได้ออกมาในรูป *...* จำนวนแถวคูณ 2 ลบ 3
    return '*'+'\n'+'\n'.join(immage)+'\n'+('* '*n).rstrip()+'\n'    # เป็นการบวกแถวแรก บวกใส้ข้างใน และแถวสุดท้าย


def test_triangle():

    T3 = '''*
*.*
* * *
'''

    T7 = '''*
*.*
*...*
*.....*
*.......*
*.........*
* * * * * * *
'''

    
    assert triangle(7) == T7
    assert triangle(3) == T3
    print("All OK")


if __name__ == '__main__':
    main()
