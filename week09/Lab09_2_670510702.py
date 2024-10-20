#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab09_2
# 204111 Sec 003

def main():
    life_path(134)

def life_path(n: int):          # (1+3+4+5) -> (1+3) -> (4)

    if len(str(n)) == 1:        # บวกเสร็จ นำไปเข้ากระบวนการแตก แล้วแบ่งออกมา
        return n
    new = sum(list(map(lambda x: int(x),list(str(n)))))
    return life_path(new)


if __name__ == '__main__':
    main()