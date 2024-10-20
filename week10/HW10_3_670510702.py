#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW10_2
# 204111 Sec 003
# TA 66-Film, 67-Ice

def main():
    test()

def polynomial_addition(p1: list[tuple[int, float]],p2: list[tuple[int, float]]):

    len_p1 = len(p1) 
    len_p2 = len(p2)
    p1 = sorted(p1,reverse=True)  # ก่อนใช้ merge ควรเรียงลำดับข้อมูลให้เรียบร้อยก่อน
    p2 = sorted(p2,reverse=True) 
    i=0
    j=0
    ans = []

    while i < len_p1 and j < len_p2: 
        if p1[i][0] == p2[j][0]:                        # ถ้าเลขยกกำลังมีค่าเท่ากัน (2,3) (2,9) 
            ans.append((p1[i][0],p1[i][1]+p2[j][1]))    # ให้ ans เก็บค่า [(2,12)]
            i += 1
            j += 1
        else:
            if p1[i][0] > p2[j][0]:                     # ถ้่ากำลัง p1>p2 (3,3) (2,9)
                ans.append(p1[i])                       # ให้ ans เก็บค่า [(3,3)]
                i += 1                                  # ให้ i เพิ่มขึ้นเรื่อยๆ แต่ยังใช้ค่า j เหมือนเดิม
            else:
                ans.append(p2[j])                       # ถ้่ากำลัง p1>p2 (3,3) (5,9)
                j += 1                                  # ให้ j เพิ่มขึ้นเรื่อยๆ แต่ยังใช้ค่า i เหมือนเดิม

    if i < len_p1: 
        ans = list(filter(lambda x : x[1] != 0,ans))    # กรณีที่ p2 คิดหมดก่อน โดยที่สปส != 0
        return ans + p1[i:]                                 # ให้ ans(ค่าที่คิดมาก่อนหน้า) + p1 ที่เหลือ
    if j < len_p2: 
        ans = list(filter(lambda x : x[1] != 0,ans))    # กรณีที่ p1 คิดหมดก่อน โดยที่สปส != 0
        return ans + p2[j:]                                 # ให้ ans(ค่าที่คิดมาก่อนหน้า) + p2 ที่เหลือ

    ans = list(filter(lambda x : x[1] != 0,ans))        # กรณีที่ p1, p2 หมดพร้อมกัน โดยที่สปส != 0
    return ans


def test():
    assert polynomial_addition([(2, 6), (1, 34), (0, -8)],[(2, -6), (0, 2), (1, 1)]) == [(1, 35), (0, -6)]
    assert polynomial_addition([(3, 3), (2, -2), (0, -7)],[(3, 2), (1, 1), (0, 7)]) == [(3, 5), (2, -2), (1, 1)]
    assert polynomial_addition([(2, 0), (1, -1)],[(1, 1), (0, 7)]) == [(0, 7)]
    print('"SA TUUUU 99"')

if __name__ == '__main__':
    main()