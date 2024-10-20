#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Hw15_2
# 204111 Sec 003

from functools import reduce
import math

def main():
    histogram((62, 49, 75, 86, 71, 63, 74, 42, 57, 75,
               56, 58, 67, 78, 63, 73, 60, 49, 66, 77,
               47, 69, 74, 63, 65, 64, 55, 52, 52, 57,
               86, 75, 68, 70, 34, 34, 68, 46, 60, 56,
               60, 65, 66, 70, 64, 84, 61, 46, 60, 76,
               59, 64, 68, 69, 68, 47, 72, 80, 11, 44,
               53, 70, 50, 79, 81, 68, 75, 48, 62, 68))
    histogram((19, 39, 59, 42, 42, 42, 100,1))
    histogram((1,)*100 + (10,)*100 + (100,)*100)

def histogram(scores: list[int]):
   
    period = [] # [0, 1, 0, 2, 9, 11, 26, 16, 5, 2]
    for i in range(10):
        if i < 9:
            period.append(len(list(filter(lambda x: x >= i*10 and x <= (i*10)+9, scores))))
        elif i == 9:
            period.append(len(list(filter(lambda x: x >= i*10 and x <= (i*10)+10, scores))))
    
   
    hight = list(map(lambda x: math.ceil((x/5)),period)) # [0, 1, 0, 1, 2, 3, 6, 4, 1, 0]
    maxi = max(hight)
    minus = list(map(lambda x: maxi - x, hight)) # [6, 5, 6, 5, 4, 3, 0, 2, 5, 6]
    tup = list(zip(minus, period, hight)) 
    # [(6, 0, 0), (5, 1, 1), (6, 0, 0), (5, 2, 1), (4, 9, 2), (3, 11, 3), (0, 26, 6), (2, 16, 4), (5, 5, 1), (6, 0, 0)]
    

    '''
                                      26
                                     _____ 
                                    |*****| 16
                                11  |*****|_____
                           9   _____|*****|*****|
         1           2   _____|*****|*****|*****|  5
   0   _____   0   _____|*****|*****|*****|*****|_____   0  
 _____|*****|_____|*****|*****|*****|*****|*****|*****|_____
0     10    20    30    40    50    60    70    80    90    100

    '''

    dot = []
    for i in tup:
        if len(str(i[1])) == 1:
            num = ['@ '+str(i[1])+' @']
        elif len(str(i[1])) == 2:
            num = ['@'+str(i[1])+' @']
        else:
            num = ['@'+str(i[1])+'@']

        dot.append(['@   @']*i[0] + num + ['#___#'] + ['|*****|']*i[2])

    text = list(zip(*dot))
    summ = []
    for i in text:
        summ.append('a' + reduce(lambda x,y: x+y,i))
    


    solut = '\n'.join(summ).replace('@#','  #').replace('#@','#  ').replace('a@','a  ')\
                           .replace('@@','   ').replace('||','|').replace('@',' ').replace('a#','a _')\
                           .replace('##','_ _').replace('#','_').replace('a','')
    print(solut)

    under = '0     10    20    30    40    50    60    70    80    90    100'
    print(under)









    # dot = []
    # for i in range(len(tup)):
    #     if i == 0:
    #         if tup[i][1] < 10:
    #             dot.append(['^^^^^^']*tup[i][0] + ['...'+str(tup[i][1])+'...'] + [' _____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['^^^^^^']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + [' _____'] + ['|*****|']*tup[i][2])
        

    #     elif i < len(tup)-1 and tup[i-1][1] == 0 and tup[i][1] > 0 and tup[i+1][1] == 0:
    #         if tup[i][1] < 10:
    #             dot.append(['777777']*tup[i][0] + ['...'+str(tup[i][1])+'..'] + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['777777']*tup[i][0] + ['..'+str(tup[i][1])+'..'] + ['_____'] + ['|*****|']*tup[i][2])




    #     elif i < len(tup)-1 and tup[i-1][1] == 0 and tup[i][1] == 0 and tup[i+1][1] == 0:
    #         dot.append(['      ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + [' _____'])

        
    #     elif i < len(tup)-1 and tup[i-1][1] == 0 and tup[i][1] == 0 and tup[i+1][1] > 0:
    #         dot.append(['      ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + [' _____'])


    #     # elif i < len(tup)-1 and tup[i][1] == 0:
    #     #     dot.append(['       ']*tup[i][0] + ['...'+str(tup[i][1])+'...'] + ['_____'])

    #     elif i < len(tup)-1 and tup[i-1][1] > 0 and tup[i][1] == 0 and tup[i+1][1] > 0:
    #         dot.append(['+++++++']*tup[i][0] + ['...'+str(tup[i][1])+'...'] + ['_____'])





    #     elif i == len(tup)-1 and tup[i-1][1] == 0 and tup[i][1] > 0 :
    #         if tup[i][1] < 10:
    #             dot.append(['&&&&&']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['&&&&&']*tup[i][0] + ['.'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])



    #     elif i < len(tup)-1 and tup[i-1][1] > 0 and tup[i][1] > 0 and tup[i+1][1] == 0 :
    #         if tup[i][1] < 10:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'..'] + [' _____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['     ']*tup[i][0] + ['.'+str(tup[i][1])+'.. '] + [' _____'] + ['|*****|']*tup[i][2])

        

    #     elif i < len(tup)-1 and tup[i-1][2] < tup[i][2] and tup[i+1][2] > tup[i][2]:
    #         if tup[i][1] < 10:
    #             dot.append(['######']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['######']*tup[i][0] + ['.'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])


    #     elif i < len(tup)-1 and tup[i-1][2] < tup[i][2] and tup[i+1][2] < tup[i][2]:
    #         if tup[i][1] < 10:
    #             dot.append(['=====']*tup[i][0] + ['...'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['=====']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])



    #     elif i < len(tup)-1 and tup[i-1][2] > tup[i][2] and tup[i+1][2] < tup[i][2]:
    #         if tup[i][1] < 10:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['     ']*tup[i][0] + ['.'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])



    #     elif i < len(tup)-1 and tup[i-1][2] == tup[i][2]:
    #         if tup[i][1] < 10:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + [' _____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['     ']*tup[i][0] + ['.'+str(tup[i][1])+'...'] + [' _____'] + ['|*****|']*tup[i][2])

    #     elif i < len(tup)-1 and tup[i-1][2] == 0 and tup[i][2] ==tup[i+1][2]:
    #         if tup[i][1] < 10:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #              dot.append(['     ']*tup[i][0] + ['.'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])


 
    #     else:
    #         if tup[i][2] >= 0 and tup[i][2] < 10:
    #             dot.append(['$$$$$']*tup[i][0] + ['...'+str(tup[i][1])+'...']  + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #             dot.append(['$$$$$']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])


    # text = list(zip(*dot))
    # summ = []
    # for i in text:
    #     summ.append(reduce(lambda x,y: x+y,i))
    


    # solut = '\n'.join(summ)
    # print(solut)

    # under = '0     10    20    30    40    50    60    70    80    90    100'
    # print(under)



    # dot = []
    # for i in range(len(tup)):
    #     if i == 0:
    #         dot.append(['######']*tup[i][0] + ['...'+str(tup[i][1])+'...']  + [' _____'] + ['|*****|']*tup[i][2])


    #     elif i < len(tup)-1 and tup[i+1][2] != 0  and tup[i-1][2] != 0:

    #         if tup[i][2] >= 0 and tup[i][2] < 10:
    #             dot.append(['     ']*tup[i][0] + ['...'+str(tup[i][1])+'...']  + ['_____'] + ['*****|']*tup[i][2])
    #         else:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['*****|']*tup[i][2])


    #     # elif i < len(tup)-1 and tup[i+1][1] > tup[i][1] and tup[i+2][1] > tup[i][1] and tup[i][1] > tup[i-1][1]:

    #     #     if tup[i][1] >= 0 and tup[i][1] < 10:
    #     #         dot.append(['     ']*tup[i][0] + ['...'+str(tup[i][1])+'...'] + ['*****|']*tup[i][2])
    #     #     else:
    #     #         dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['*****|']*tup[i][2])



    #     elif i < len(tup)-1 and tup[i+1][2] < tup[i][1]  and tup[i][2] < tup[i-1][2]:

    #         if tup[i][2] >= 0 and tup[i][2] < 10:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...']  + ['_____'] + ['*****|']*tup[i][2])
    #         else:
    #             dot.append(['     ']*tup[i][0] + ['.'+str(tup[i][1])+'...'] + ['_____'] + ['*****|']*tup[i][2])

    #     else:
    #         if tup[i][2] >= 0 and tup[i][2] < 10:
    #             dot.append(['     ']*tup[i][0] + ['...'+str(tup[i][1])+'...']  + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])

        
    # text = list(zip(*dot))
    # summ = []
    # for i in text:
    #     summ.append(reduce(lambda x,y: x+y,i))
    # summ = list(map(lambda x: x.replace('_*','_|*').replace('.*','.|*').replace(' *',' |*'), summ))
    # print(summ)
    

    # solut = '\n'.join(summ)
    # print(solut)

    # under = '0     10    20    30    40    50    60    70    80    90    100'
    # print(under)


    # dot = []
    # for i in range(len(tup)):
    #     if i == 0:
    #         dot.append(['      ']*tup[i][0] + ['...'+str(tup[i][1])+'...']  + [' _____'] + ['|*****|']*tup[i][2])
          
        
    #     elif i < len(tup)-1 and tup[i+1][1] == 0 and tup[i][1] > tup[i-1][1] or tup[i-1][1] == 0 :
    #         if tup[i][1] >= 0 and tup[i][1] < 10:
    #             dot.append(['     ']*tup[i][0] + ['...'+str(tup[i][1])+'...']  + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])
    #     else:
    #         if tup[i][1] >= 0 and tup[i][1] < 10:
    #             dot.append(['     ']*tup[i][0] + ['...'+str(tup[i][1])+'...']  + ['_____'] + ['|*****|']*tup[i][2])
    #         else:
    #             dot.append(['     ']*tup[i][0] + ['..'+str(tup[i][1])+'...'] + ['_____'] + ['|*****|']*tup[i][2])


 

    # text = list(zip(*dot))
    # summ = []
    # for i in text:
    #     summ.append(reduce(lambda x,y: x+y,i))
    # summ = list(map(lambda x: x.replace('||','|').replace('|.','|'), summ))
    

    # solut = '\n'.join(summ)
    # print(solut)

    # under = '0     10    20    30    40    50    60    70    80    90    100'
    # print(under)

'''
    dot = []
    for i in range(len(tup)):
        if i == 0:
            dot.append(['......']*tup[i][0] + ['...'+str(tup[i][1])+'..'] + ['.......'] + [' _____'] + ['|*****|']*tup[i][2])
        elif i == len(tup)-1:
            dot.append(['......']*tup[i][0] + ['...'+str(tup[i][1])+'..'] + [('.' if tup[i][1] < tup[i-1][1] else '') + '.....' ] + ['_____'] + ['|*****|']*tup[i][2])
            



        else:
            if tup[i][1] > 0 and tup[i][1] < 10:
                dot.append(['......']*tup[i][0] + ['...'+str(tup[i][1])+'..'] + [('.' if tup[i][1] 
                < tup[i-1][1] else '') + '.....' + ('.' if tup[i][1] < tup[i+1][1] else '')] + ['_____'] + ['|*****|']*tup[i][2])
            else:
                dot.append(['......']*tup[i][0] + ['..'+str(tup[i][1])+'..'] + [('.' if tup[i][1] 
                < tup[i-1][1] else '') + '.....'+ ('.' if tup[i][1] < tup[i+1][1] else '')] + ['_____'] + ['|*****|']*tup[i][2])
 

    text = list(zip(*dot))
    summ = []
    for i in text:
        summ.append(reduce(lambda x,y: x+y,i))
    # print(summ)
    summ = list(map(lambda x: x.replace('||','|').replace('|.','|'), summ))

    solut = '\n'.join(summ)
    print(solut)

    under = '0     10    20    30    40    50    60    70    80    90    100'
    print(under)


'''


if __name__ == '__main__':
    main()