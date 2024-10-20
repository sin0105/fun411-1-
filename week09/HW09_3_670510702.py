#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW09_3
# 204111 Sec 003

def main():
    print(unmask_id('*-2345-67890-1*-*'))


def algo(new):
        last = int(new[-1]) 
        new = new[:-1]
        a = list(map(lambda x: int(new[x])*(13-x),range(0,12)))
    
        c = (11-(sum(a) % 11))%10
        if c == last:
            return True
        else: return False


def unmask_id(masked_id: str):
    text = masked_id.replace('-','').replace('*','{}')                                         # {} เตรียมใส่ค่า
    num = list(map(lambda x: str(x).zfill(text.count('{}')),range(0,10**text.count('{}'))))    # 001 002 003
    new = list(map(lambda x: text.format(*str(x)),num))                                        # นำเลขมาใส่ {}
    true = list(filter(lambda x: algo(x) == True,new))                                         # เลือกเฉพาะตัวที่เป็นจริงออกมา
    
    before = list(filter(lambda x: x[0] != '0',true))
    result = list(map(lambda x: x[0] + '-' + x[1:5] + '-' + x[5:10] + '-' + x[10:12] + '-' + x[-1],before))
    return result


if __name__ == '__main__':
    main()