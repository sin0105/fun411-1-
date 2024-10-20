#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW12_1
# 204111 Sec 003
# TA 66-Film

def main():
    test()
    # print(scramble('ABCDE'))

def scramble(word: str):
    if len(word) == 1:          # หยุดรีเคอชัน และส่งข้อมูล
        return set(word)

    head = word[0]              # A
    tail = word[1:]             # BCDE

    result = set()
    word_head = set()
    word_tail = scramble(tail)  # นำ BCDE รีเคอชันต่อ 
    for i in word_tail:                         # tail: DE
        for j in range(len(i)+1):               # head: C
           result |= {i[:j] + head + i[j:]}     # result: CDE DCE DEC

    result = sorted(set(result)) # เรียงข้อมูล
    return result


def test():
    assert scramble('Cat') == ['Cat', 'Cta', 'aCt', 'atC', 'tCa', 'taC']
    assert scramble('bee') == ['bee', 'ebe', 'eeb']
    assert scramble('bEe') == ['Ebe', 'Eeb', 'bEe', 'beE', 'eEb', 'ebE']
    print('mia dai kin pom')
    
if __name__ == '__main__':
    main()







