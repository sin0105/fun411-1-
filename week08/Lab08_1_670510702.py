#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab08_1
# 204111 Sec 003

def main():
    test()

def gcd(x: int, y: int):
    x, y = abs(max(x,y)), abs(min(x,y))
    if x % y == 0:
        return y 
    return gcd(x%y,y)
 
def test():
    assert gcd(19,71) == 1
    assert gcd(-39,78) == 39
    assert gcd(66,11) == 11
    print("ALL OK BROTHER")

if __name__ == '__main__':
    main()