#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW10_EX
# 204111 Sec 003

cat_l = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''
cat_r = \
    '''| ／|、    
|(°、。7   
| |、 ~ヽ  
| ᒐᒐ_f_ )ノ
|__________
'''
cat_f = \
    ''' ／|、    
(°、。7   
 |、 ~ヽ  
 ᒐᒐ_f_ )ノ
__________
'''



def main():
    print(cat_altar(int(input())))


def cat_altar(n):
    result = ''
    cat_1 = '+'*(((n-1)*10)+(n-1)) + cat_f[:9] + '+'*(((n-1)*10)+(n-1))+ cat_f[9:18] + \
            '+'*(((n-1)*10)+(n-1)) + cat_f[18:27] +'+'*(((n-1)*10)+(n-1)) +cat_f[27:37] + \
            '+'*(((n-1)*10)+(n-1)) +cat_f[37:]


    for i in range(1,n):
        cat_m = '+'*(((n-(i+1))*10)+(n-(i+1))) + cat_l[:9] + '+'*((10*((2*i)-1)) + ((2*i)-2)) +cat_r[:9]+cat_l[9]+ \
                '+'*(((n-(i+1))*10)+(n-(i+1)))+cat_l[10:19] + '+'*((10*((2*i)-1)) + ((2*i)-2)) + cat_r[10:19]+ cat_l[19]+\
                '+'*(((n-(i+1))*10)+(n-(i+1)))+cat_l[20:29] +'+'*((10*((2*i)-1)) + ((2*i)-2)) + cat_r[20:29] +cat_l[29]+\
                '+'*(((n-(i+1))*10)+(n-(i+1)))+cat_l[30:40] + '+'*((10*((2*i)-1)) + ((2*i)-2))+ cat_r[30:40] +cat_l[40]+\
                '+'*(((n-(i+1))*10)+(n-(i+1)))+cat_l[41:52] + '+'*((10*((2*i)-1)) + ((2*i)-2)) + cat_r[41:]
        result = result + cat_m

    return cat_1.replace('+'," ") + result.replace('+'," ")

if __name__ == '__main__':
    main()



