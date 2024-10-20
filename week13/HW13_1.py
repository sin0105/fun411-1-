#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW13_2
# 204111 Sec 003
# TA-66 Film, TA-67 Tan


def main():
    print(count_vote([['Mewtwo', 'Pikachu', 'Suicune'], 
                    ['Mewtwo', 'Suicune', 'Pikachu'], 
                    ['Pikachu', 'Rayquaza', 'Charizard'], 
                    ['Suicune', 'Pikachu', 'Charizard']]))
    '''
             [0]     [1]       [2]        [3]
      [0] [['-1', 'Suicune', 'Pikachu', 'Mewtwo'], 
      [1] ['-1', 'Pikachu', 'Suicune', 'Mewtwo'], 
      [2] ['-1', 'Charizard', 'Rayquaza', 'Pikachu'], 
      [3] ['-1', 'Charizard', 'Pikachu', 'Suicune']]
    '''

def count_vote(pref_matrix: list[list[str]]):
    rev = []
    for i in pref_matrix:
        rev.append(['-1']+i[::-1])

    rev_set = tuple()
    for i in pref_matrix:
        rev_set+=(tuple(i))
    rev_set = set(rev_set)

    list_rev = []
    for i in rev_set:
        list_rev.append(i)
    #['Pikachu', 'Rayquaza', 'Mewtwo', 'Charizard', 'Suicune']

    dic = dict()
    for i in rev:
        for j in range(len(i)): # 0, 1, 2, 3
            dic[i[j]] = j + dic.get(i[j],0)
     

    solute = sorted(map(lambda x: (x,dic[x]),list_rev))
    result = sorted(solute, key=lambda x: x[1], reverse=True)
    return result

if __name__ == '__main__':
    main()
