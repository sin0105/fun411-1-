#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab10_1
# 204111 Sec 003

def main():
    test()
    print(comma_separated(1234567,4))


def comma_separated(n: int, group: int=3):              # คิดจากท้ายมาข้างหน้า
    text = str(n)
    ans = ''                                            # ตัวเก็บค่า
    for index,word in enumerate(reversed(text)):        # ใช้ enumerate เก็บ ตน.ใน index, เก็บ ตัวเลขใน word
        if index % group == 0 and index != 0:           # หากค่า index % จน.ที่รับมา ลงตัว โดไม่คิด index=0 
            ans = word + ',' + ans                          # => 3(,)4567
        else:
            ans = word + ans                                # => 123(,)4567
    return ans


def test():
    assert comma_separated(3400,3) == '3,400'
    assert comma_separated(3400,4) == '3400'
    assert comma_separated(781588,5) == '7,81588'
    assert comma_separated(1234) == '1,234'
    assert comma_separated(1000000) == '1,000,000'
    print("SA TUUUU 99")

if __name__ == '__main__':
    main()