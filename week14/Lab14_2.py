#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab14_2
# 204111 Sec 003
# TA-67 Ton

def main():
    list_x = [('11/Jan/1900', 'Event A'), ('5/Dec/2001', 'Event B'),
              ('5/Dec/2002', 'Event C'), ('21/Aug/2008', 'Event D'),
              ('9/Mar/2013', 'Event E'), ('11/Mar/2017', 'Event F'),
              ('7/May/2019', 'Event G'), ('29/Feb/2032', 'Event H'),
              ('9/Nov/2042', 'Event I')]
    event = search_event(list_x, '29/Feb/2032', show_steps = True)
    # event = search_event(list_x, '23/Aug/2008', show_steps = True)
    # event = search_event(list_x, '7/May/2019', show_steps = False)
    print('---')
    print(event)
    

def search_event(list_x: list[tuple[str]], key: str, show_steps: bool=False):
    lo = 0
    hi = len(list_x) - 1
    found = False
    while lo <= hi and not found:
        mid = (lo + hi) // 2
        if key == list_x[mid][0]:
            found = True
        elif less_than(key, list_x[mid][0]):
            hi = mid - 1
        else:
            lo = mid + 1
        if show_steps == True:
            print(str([mid]) + ': ' +list_x[mid][0])

    if found == False:
        result = None
    elif found == True:
        result = list_x[mid]

    return result


def less_than(key, solution):
    # print(solution)
    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
             'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
             'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    key = key.split('/')
    key = int(key[-1] + month[key[1]] + key[0].zfill(2))

    solution = solution.split('/')
    solution = int(solution[-1] + month[solution[1]] + solution[0].zfill(2))

    if key < solution:
        return True
    elif key > solution: 
        return False
   

if __name__ == '__main__':
    main()