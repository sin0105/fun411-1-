#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab14_1
# 204111 Sec 003
# TA-67 Tan

def main():
    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    # list_x = ['5/ธ.ค./2542','5/ธ.ค./2542','5/ธ.ค./2542','5/ธ.ค./2542','5/ธ.ค./2542']
    sort_date(list_x,show_steps=True)
    print("---")
    print(list_x)
    

def sort_date(list_x: list[str], show_steps: bool=False):
    month = {'ม.ค.': '01', 'ก.พ.': '02', 'มี.ค.': '03', 'เม.ย.': '04',
             'พ.ค.': '05', 'มิ.ย.': '06', 'ก.ค.': '07', 'ส.ค.': '08',
             'ก.ย.': '09', 'ต.ค.': '10', 'พ.ย.': '11', 'ธ.ค.': '12'}
    day = list(map(lambda x: x.split('/'), list_x))
    # [['11', 'ม.ค.', '2643'], ['5', 'ธ.ค.', '2542'], ['19', 'ม.ค.', '2546'], ['11', 'ก.ย.', '2544']]

    solution = list(map(lambda x: int(x[-1] + month[x[1]] + x[0].zfill(2)),day))
    # [2643111, 25421205, 2546119, 2544911]

    
    dic = dict()
    for i in range(len(list_x)):
        dic[solution[i]] = list_x[i]
    # {26430111: '11/ม.ค./2643', 25421205: '5/ธ.ค./2542', 25460119: '19/ม.ค./2546', 25440911: '11/ก.ย./2544'}
    
    size = len(solution)
    text = solution[:] 

    for i in range(1, size): 
        j = i
        while j > 0 and text[j] < text[j-1]:
            text[j], text[j-1] = text[j-1], text[j] 
            j -= 1

        check = list(map(lambda x: dic[x], text))
        if show_steps == True:
            print(str(i)+':',check)
    list_x[:] = check


if __name__ == '__main__':
    main()
