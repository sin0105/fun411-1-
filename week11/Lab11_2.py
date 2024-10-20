#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab_2
# 204111 Sec 003
# TA 66-Film , TA 65-Kla

def main():
    test()
    print(matching_sum((5, 2), 7))


def matching_sum(t: tuple[int], target_value: int):
    new = set()
    for num in t:
        if target_value - num in new :          # (7-5)=2 in  (5,2)
            return [num , target_value - num]   # [5, 2]
        new.add(num)
    return []

def test():
    assert matching_sum((1,), 1) == []
    assert matching_sum((5, 2), 7) in ([5, 2], [2, 5])
    assert matching_sum((99, 10, -1, 1, -8, 3, 1), 2) in ([10, -8], [-8, 10], [-1, 3], [1, 1])
    assert matching_sum((10, -1, 1, -8, 3, 1), 10) == []
    assert matching_sum((5,), 10) == []

    print('pai non dai')




if __name__ == '__main__':
    main()

