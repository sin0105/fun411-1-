#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW10_2
# 204111 Sec 003
# TA 66-Film, TA 67-Noon

def main():
    test()
    # print(arrival_sequences(('A', 'B'), ('c', 'd')))


def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str], result = []):

    if len(l_lane) == 0:                # กรณีเลนซ้ายหมด
        result += r_lane                # ค่าที่เก็บไว้ + เลนขวาที่เหลือ
        result = '>'.join(result)
        return [result]

    if len(r_lane) == 0:                # กรณีเลนขวาหมด
        result += l_lane                # ค่าที่เก็บไว้ + เลนซ้ายที่เหลือ
        result = '>'.join(result)
        return [result]

    left = arrival_sequences(l_lane[1:], r_lane, result + [l_lane[0]])  # ซ้าย : ให้วนซ้ายไปเรื่อยๆ เลนขวาอยู่เหมือนเดิม result เก็บค่าเลนซ้าย ตน.ไปเรื่อยๆ 
    right = arrival_sequences(l_lane,r_lane[1:], result + [r_lane[0]])  # ขวา : ให้วนขวาไปเรื่อยๆ เลนซ้ายอยู่เหมือนเดิม result เก็บค่าเลนขวา ตน.ไปเรื่อยๆ 
    result = left + right   # นำซ้าย + ขวา เพิ่อส่งไปคิดใหม่
    return result


def test():
    assert arrival_sequences(('A',), ('b', 'c')) == ['A>b>c', 'b>A>c', 'b>c>A']
    assert arrival_sequences(('A', 'B'), ('c', 'd')) == ['A>B>c>d', 'A>c>B>d', 'A>c>d>B', 'c>A>B>d', 'c>A>d>B', 'c>d>A>B']
    print("SA TUUUU 99")

if __name__ == '__main__':
    main()
