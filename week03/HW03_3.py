#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW03_3
# 204111 Sec 003

def main():
     number = (int(input()))
     k = int(input())
     value = int(input())
     print(set_kth_digit(number,k,value))
   


def kth_digit(number: int, k: int):
    number = abs(number)
    result = (number%(10**(k+1))//(10**(k))) 
    return result

def set_kth_digit(number: int, k: int, value:int):
    new = kth_digit(number,k)
    ans = (number-(new*(10**k))+(value*10**k))
    return ans


if __name__ == '__main__':
    main()