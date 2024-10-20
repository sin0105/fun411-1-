#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW04_2
# 204111 Sec 003
# TA Film

def main():
    test_minute_diff()


# implement this function
def minute_diff(h1: int, m1: int, p1: str,
                h2: int, m2: int, p2: str) -> int:
    if p1 == "PM" and h1!=12:               # กรณี PM ให้+12 แต่เมื่อเป็นเที่ยงวัน 12 นาฬิกาจะไม่บวกเพิ่ม12
        h1 += 12
    if p2 == "PM" and h2!=12:
        h2 += 12

    if p1 == "AM" and h1==12:              # กรณี AM ให้แปลงค่า h=0 เพราะเป็นเที่ยงคืน 12 นาฬิกา ให้เริ่มใหม่เป็น 0
        h1 = 0
    if p2 == "AM" and h2==12:
        h2 = 0   

    result = abs((h1*60+m1)-(h2*60+m2)).   # แปลงค่าทั้งหมดเป็นหน่วยนาที
    return result



# test function
def test_minute_diff():
    assert minute_diff(8, 23, "AM", 8, 24, "AM") == 1
    assert minute_diff(8, 23, "AM", 1, 24, "PM") == 301
    assert minute_diff(1, 24, "PM", 8, 23, "AM") == 301
    assert minute_diff(1, 00, "AM", 12, 00, "PM") == 660
    assert minute_diff(12, 00, "PM", 12, 00, "AM") == 720
    assert minute_diff(12, 00, "AM", 12, 00, "PM") == 720
    assert minute_diff(2, 58, "AM", 12, 00, "PM") == 542
    assert minute_diff(1, 59, "AM", 12, 00, "PM") == 601
    assert minute_diff(11, 59, "AM", 12, 00, "PM") == 1
    assert minute_diff(11, 59, "PM", 12, 00, "PM") == 719      # เทสนี้แจ่มสุด
    assert(minute_diff(0, 30, "AM", 11, 30, "PM")) == 1380     # เทสนี้แจ่มสุด
    assert(minute_diff(11, 30, "PM", 0, 30, "AM")) == 1380
    assert(minute_diff(0, 0, "AM", 12, 0, "PM")) == 720
    assert(minute_diff(12, 0, "PM", 12, 0, "AM")) == 720
    assert(minute_diff(0, 0, "AM", 0, 0, "PM")) == 720
    assert(minute_diff(0, 0, "AM", 0, 0, "AM")) == 0
    assert(minute_diff(12, 0, "AM", 12, 0, "PM")) == 720
    assert(minute_diff(8, 24, "AM", 12, 35, "PM")) == 251
    assert(minute_diff(1, 59, "PM", 2, 0, "PM")) == 1

   


    print("all ok!")


if __name__ == "__main__":
    main()
