#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW03_2
# 204111 Sec 003

def main():
     number = (int(input()))
     k = int(input())
     print(kth_digit(number,k))
   



def kth_digit(number: int, k: int):
    number = abs(number)
    result = (number%(10**(k+1))//(10**(k)))
    return result


if __name__ == '__main__':
    main()