#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab09_1
# 204111 Sec 003

def main():
    patterned_message("123", "** *** ** ** *")
    patterned_message("D and C",'''
***************
******   ******
***************
''')
    patterned_message("Three Diamonds!",'''
  *     *     *
 ***   ***   ***
***** ***** *****
 ***   ***   ***
  *     *     *
''')

def patterned_message(message: str, pattern:str, mark: str=''):
    if len(pattern) == 0:
        print(mark) 
        return                                      # หยุดเถอะอานนท์

    message = message.replace(' ','')
    head = pattern[0]
    if head == '\n':                                # ('\n') ให้ mark เป็น '\n'
        mark += '\n'                                
    elif head == ' ':                               # (' ')  ให้ mark เป็น ' '
        mark += ' '                                 
    else:                                           # (*)
        mark += message[0]                            # ให้ mark ใช้ message ตำแหน่งที่ 0
        message = message[1:] + message[0]            # เปลี่ยน message ให้วนข้อความ เอาหัวไปต่อท้าย

    pattern = pattern[1:]
    return patterned_message(message,pattern,mark)

if __name__ == '__main__':
    main()
