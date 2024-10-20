#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW08_2
# 204111 Sec 003

def main():
    test()


def skip_list(word: str, n: int = 0):
    # base case
    if n > len(word)-1:
        return []

    # d & c
    result = []
    head = word[n::n+1]
    tail = skip_list(word,n+1)

    # combine
    result.append(head)
    result.extend(tail)
    return result


def test():
    assert skip_list('ABCD') == ['ABCD', 'BD', 'C', 'D']
    assert skip_list('hello!') == ['hello!', 'el!', 'l!', 'l', 'o', '!']
    assert skip_list('a') == ['a']
    print("ALL OK BROTHER")

if __name__ == '__main__':
    main()