#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW11_3
# 204111 Sec 003
# TA 66-Film

def runner_up():
    total = int(input('Total students: ')) 
    sum_ = 0
    maxx = 0
    runner = 0

    print('Enter score: ')
    for i in range(total): 
        current_score = float(input()) 
        sum_ = sum_ + current_score

        if current_score > maxx: 
            runner = maxx                
            maxx = current_score        
            '''
            3, 4, 5, 7, 6
            run = 0  
            max = 3 ->run = 3  
                      max = 4 -> run = 4
                                 max = 5 -> run = 5
                                            max = 7
            '''
        if current_score > runner and current_score < maxx:
            runner = current_score
            '''
                                            run = 5
                                            max = 7 -> run = 6
                                                       max = 7 
            '''
    
    if runner == 0:
        runner = None
    else:
        runner = "{:.2f}".format(runner)

    print('---')
    print(f'Max score is: {maxx:.2f}')
    print(f'Runner up is: {runner}')
    print(f'Average is: {sum_/total:.2f}')


if __name__ == '__main__':
    runner_up()
