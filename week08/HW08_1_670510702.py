#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW08_1
# 204111 Sec 003

from math import isclose
def main():
    test_pi()


def pi(n):
    # base case
    if n == 0:
        return 3
    if n % 2 == 0:
        return pi(n-1) - 4/(((n*2)*((n*2)+1)*((n*2)+2)))
    else:
        return pi(n-1) + 4/(((n*2)*((n*2)+1)*((n*2)+2)))


def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")


if __name__ == '__main__':
    main()

