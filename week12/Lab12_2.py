#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab12_2
# 204111 Sec 003
# TA 67-Noon

def main():
    print(multiply_polynomials([2, 0, 3], [4, 5]))


def multiply_polynomials(p1: list[int], p2: list[int]):
    first = list(zip(p1, list(range(len(p1))[::-1])))   # จับคู่ p1 กับ range ย้อนกลับ -> 3 2 1 0
    second = list(zip(p2, list(range(len(p2))[::-1])))  # จับคู่ p2 กับ range ย้อนกลับ -> 3 2 1 0

    coef = []
    power = []
    dicts = {}
    for i in range(len(first)):
        for j in range(len(second)):
            coef = first[i][0] * second[j][0]           # นำสปส.( coef )มาคูณกัน
            power = first[i][1] + second[j][1]          # นำเลขยกกำลังมาบวกกัน
            if power in dicts:                          # ถ้ามีกำลัง ที่เท่ากันอยู่แล้ว   
                dicts[power] += coef                          # ให้สปส.ในกำลังนั้น บวกกัน
            else:
                dicts[power] = coef                      # หากไม่มี ให้สปส.ในกำลังนั้นเป็นตัวเดิม

    result = list(map(lambda x: dicts[x],dicts))
    return result

if __name__ == '__main__':
    main()