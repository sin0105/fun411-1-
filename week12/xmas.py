#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# EX xmas_tree
# 204111 Sec 003

def main():
    print(xmas_tree(13))

def xmas_tree(n: int):


    a = '     |   '
    b = '   --*-- '
    c = '    /|\\  '
    d = '   /* *\\ '
    e = '  /* * *\\'
    f = ' /* * * *\\'
    g = '/* * * * *\\'
    h = '    |||'
    i = '____|||____'

    on_top = []                             # ด้านบน a,b,c,d เพิ่มแค่ช่องว่างข้างหน้า
    for top in [a,b,c,d]:
        on_top += [' '*(n-1) + top]

    on_row = []
    for mid in range(1,n+1):                # ตรงกลาง e,f,g 
        for row in [e,f,g]: 
            on_row += [' '*(abs(n-mid)) + row[:-1] + ' *'*(mid-1) + row[-1:]]
   
    under1 = (' '*(n-1)) + h                # ฐานต้นไม้ เพิ่มขีด หน้า-หลัง
    under2 = ('_'*(n-1)) + i + ('_'*(n-1))
    under = [under1, under2]
   
    result = '\n'.join(on_top + on_row + under)
    return '\n' + result
   

if __name__ == '__main__':
    main()
