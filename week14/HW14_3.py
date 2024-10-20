#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Hw14_3
# 204111 Sec 003
# TA-66 Film

import string
def main():
    list_x = ['beer', 'wine', 'vinegar', 'vodka']
    radix_word(list_x, True)
    print('--------')
    print(list_x)

def radix_word(list_x: list[str], show_steps=False):
    dic = {x: [] for x in ' ' + string.ascii_lowercase}
    '''
    {' ': [], 'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 
    'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 
    'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
    '''
    maxx = max(map(lambda x: len(x),list_x))
    empty = list(map(lambda x: maxx - len(x),list_x))
    plus = []
    for n in range(len(list_x)):
        plus.append(list_x[n] + (' '*empty[n]))
    
    for i in range(-maxx,0)[::-1]:
        for j in plus:
            dic[j[i]] += [j]

        keep = []
        for k in dic.values():
            keep += k 
        dic = {x: [] for x in ' ' + string.ascii_lowercase}

        show = list(map(lambda x: x.strip(),keep))
        if show_steps == True:
            print(show)

    list_x[:] = show


if __name__ == '__main__':
    main()