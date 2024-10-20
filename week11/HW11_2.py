#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW11_2
# 204111 Sec 003
# TA 65-Kla ,TA 66-Film, TA 67-Tan, TA 67-Ton, TA Ice
# รถแง้น ( v.2 )

def main():
    print(split_and_merge(3))
    # print(find_powerset_([1,2,3]))

DEBUG = False
def split_and_merge(n: int):
    list_num = list(map(str,range(1,n+1)))  
    if DEBUG: print('list_num : ',list_num)
        # ['1', '2', '3']             
    
    solution1 = (find_powerset_(list_num))[1:-1]    # ไม่เอาตัวแรก และสุดท้าย ('1', '2', '3'), ()
    solution2 = []
    for i, solu in enumerate(reversed(solution1)):  # กลับด้าน
       solution2.append(solu)
    if DEBUG: 
        print('s1 : ',solution1)
        # [('1', '2'), ('1', '3'), ('1',), ('2', '3'), ('2',), ('3',)]
        print('s2 : ',solution2)
        # [('3',), ('2',), ('2', '3'), ('1',), ('1', '3'), ('1', '2')]

    result = set()
    all_solu = list(zip(solution1, solution2))      # ได้คู่ เลนบน-ล่าง, result ใช้ set() -> กำจัดตัวซ้ำ
    if DEBUG: print('all_solu : ',all_solu)
        # [  (('1', '2'), ('3',)), (('1', '3'), ('2',)), (('1',), ('2', '3')), 
        #    (('2', '3'), ('1',)), (('2',), ('1', '3')), (('3',), ('1', '2'))  ]
    for i in all_solu:
        result.update(set(arrival_sequences(i[0],i[1])))        # นำเลนบน-ล่าง มาคิด(arrival_sequences)(รถแง้น ( v.2 ))
    if DEBUG: print('result last : ',sorted(list(result))) 
        # ['1>2>3', '1>3>2', '2>1>3', '2>3>1', '3>1>2']
   
    return sorted(list(result))
    
    

    
def find_powerset_(list_num: list[str]):
    if not list_num:
        return [()]                         # ใช้ tuple ให้ง่ายต่อการนำไปใช้ set

    head = list_num[0]
    tail = list_num[1:]

    bus_head = []
    bus_tail = find_powerset_(tail)         # ทำจนกว่าหางจะหมด
    for item in bus_tail:
        bus_head.append((head,) + item)
        
    solution = bus_head + bus_tail
    if DEBUG:print('solution : ',solution)
        # การหา powerset แต่ได้ในรูปที่ขาดตัวคู่กัน 
        # [ ('1', '2', '3'), ('1', '2'), ('1', '3'), ('1',), ('2', '3'), ('2',), ('3',), () ]
    return solution



def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str], result = ()):
    if len(l_lane) == 0:                # เลนซ้ายหมด ให้ result ที่ทำมา + r_lane
        result += r_lane                
        result = '>'.join(result)
        return (result,)                # ใช้ tuple ให้ง่ายต่อการนำไปใช้ set

    if len(r_lane) == 0:                # เลนขวาหมด ให้ result ที่ทำมา + l_lane
        result += l_lane                
        result = '>'.join(result)
        return (result,)

    left = arrival_sequences(l_lane[1:], r_lane, result + (l_lane[0],))  # ซ้ายไปก่อน
    right = arrival_sequences(l_lane,r_lane[1:], result + (r_lane[0],))  # ซ้ายไปก่อน
    result = left + right 
    if DEBUG: print('result : ',result) 
    '''
    ถูกฟังก์ชันหลักเรียกไปใช้กับข้อมูลที่ผ่านการหา powerset มาแล้ว

    ('1>2>3', '1>3>2', '3>1>2')
    ('1>3>2', '1>2>3', '2>1>3')
    ('1>2>3', '2>1>3', '2>3>1')
    ('2>3>1', '2>1>3', '1>2>3')
    ('2>1>3', '1>2>3', '1>3>2')
    ('3>1>2', '1>3>2', '1>2>3')
    '''
    return result


if __name__ == '__main__':
    main()

