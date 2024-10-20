#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Hw14_2
# 204111 Sec 003

def main():
    list_x = [3, 7, 4, 9, 5, 2, 6]
    # list_x = [3, 7, 4, 9, 5, 2, 6, 1]
    bottom_up_m_sort(list_x, False)
    print('--------')
    print(list_x)


def bottom_up_m_sort(list_x: list[int], show_steps: bool=False):
    text = list(map(lambda x: [x],list_x))
    if show_steps == True:
        print(text)
    

    while len(text) > 1:
        if len(text) %2 == 0:
            text = list(map(lambda x: merge(text[x],text[x+1]),range(0,len(text)-1,2)))
            if show_steps == True:
                print(text)
        elif len(text) %2 != 0:
            text = (list(map(lambda x: merge(text[x],text[x+1]),range(0,len(text)-1,2))))+[text[-1]]
            if show_steps == True:
                print(text)
    list_x[:] = text[0]
  

def merge(first, sec):
    len_first = len(first)
    len_sec = len(sec)
    i = 0
    j = 0
    result = []

    while i < len_first and j < len_sec:
        if first[i] < sec[j]:
            result.append(first[i])
            i +=1
        else:
            result.append(sec[j])
            j += 1
    if i < len_first:
        return result + first[i:]
    if j < len_sec:
            return result + sec[j:]
    return result


if __name__ == '__main__':
    main()