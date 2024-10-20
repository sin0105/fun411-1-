#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab13_1
# 204111 Sec 003
# TA-66 Film, TA-67 Ton

def main():
    # matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    print(matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8, 5, 9, 3], [9, 10, -3, 7, 13], [11, 12, 6, 2, 9]]))
    # matrix_mult([[1,2,3], [4,5,6], [7,8,9]], [[1,2],[1,2],[1,2]])
    '''
    [1, 2, 3]  [ 7,  8]
    [4, 5, 6]  [ 9, 10]
               [11, 12]

    m1[0][0] * m2[0][0]
    m1[0][1] * m2[1][0]
    m1[0][2] * m2[2][0]

    m1[0][0] * m2[0][1]
    m1[0][1] * m2[1][1]
    m1[0][2] * m2[2][1]

    m1[1][0] * m2[0][0]
    m1[1][1] * m2[1][0]
    m1[1][2] * m2[2][0]

    m1[1][0] * m2[0][1]
    m1[1][1] * m2[1][1]
    m1[1][2] * m2[2][1]

    '''

def matrix_mult(m1: list[list[int]], m2: list[list[int]]):
    if len(m1) == 0 or len(m2) == 0 or len(m1[0]) != len(m2):
        return None


    find_all = []
   
    for i in range(len(m1)): #2 0,1
        for j in range(len(m2[0])):#3 0,1
            for k in range(len(m2)):#2 0,1,2
                find_all.append(m1[i][k] * m2[k][j])
    solu = list(map(lambda x: sum(find_all[x*len(m1[0]):(x*len(m1[0]))+len(m1[0])]),\
                    range(len(find_all)//len(m1[0]))))

    result = []
    for i in range(len(m1)):
        result.append(solu[i*len(m2[0]):len(m2[0])+(i*len(m2[0]))])
    return result

if __name__ == '__main__':
    main()

    # part = []
    # for i in range(len(m2[0])):
    #     part.append(find_all[i*(len(m2)*2): (i*(len(m2)*2))+(len(m2)*2)])
    # print('pa',part)

    

    # solut = []
    # for i in range(len(part)):
    #     for j in range(len(m2[0])):
    #         solut.append(sum(part[i][j:len(part[i]):len(m2)-1]))
    # print('so',solut)





    # solut = []
    # for i in range(len(part)):
    #     for j in range(len(m2[0])):
    #         solut.append(sum(part[i][j:len(part[i]):len(m2)]))
    # print('so',solut)

    # result = []
    # for i in range(len(solut)//len(m2[0])):
    #     result.append(solut[i*2:(i*2)+2])
    # print(result)


    # result = []
    # for i in range(len(m1)):
    #     for j in range(len(m2[0])):
    #         result.append(sum(part1[j:len(part1):len(m2[0])]))
    # print(result)



    # part1 = find_all[:len(find_all)//len(m1)]
    # part2 = find_all[len(find_all)//len(m1):]

    # solut1 = []
    # for i in range(len(m2[0])):
    #     solut1.append(sum(part1[i:len(part1):len(m2[0])]))

    # solut2 = []
    # for i in range(len(m2[0])):
    #     solut2.append(sum(part2[i:len(part2):len(m2[0])]))  

    # result = [solut1, solut2]   
    # return result  

