#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW08_3
# 204111 Sec 003

# DEBUG = True
DEBUG = False

def main():
    test()
    # print(is_anagram('abc def gHH!','abcdefghh'))


def is_anagram(s1: str, s2: str):
    s1 = s1.lower().replace(' ','')
    s1 = list(filter(lambda x: x.isalpha(),s1))
    s1 = ''.join(s1)
    s2 = s2.lower().replace(' ','')
    s2 = list(filter(lambda x: x.isalpha(),s2))
    s2 = ''.join(s2)
    if DEBUG:
        print(s1, s2)

    # base case
    if len(s1) != len(s2):
        return False
    if s1 == '' and s2 == '':
        return True     
    index = s1.find(s2[0])
    if index == -1:
        return False

    # d & c
    result = is_anagram(s1.replace(s1[index],'',1),s2.replace(s2[0],'',1))
    return result


def test():
    assert is_anagram('Tom Marvolo Riddle', 'I am Lord Voldemort!!!') == True
    assert is_anagram('cat', 'tab') == False
    assert is_anagram('Nissan', 'Insane') == False
    print("ALL OK BROTHER")

if __name__ == '__main__':
    main()
