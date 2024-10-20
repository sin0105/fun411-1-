#!/usr/bin/env python3

def main():
    test()


def print_polynomial(poly: list[tuple[int,float]], v: str):
    poly = list(filter(lambda x: x[1] != 0,poly))
    if poly == []:
        return '0'
    poly = sorted(poly,key=lambda x: x[0],reverse=True)
    result = list(map(lambda x: the_poly(poly,v,x),range(0,len(poly))))
    result = str(result).strip('[]').replace("'",'').replace(', ','')
    print(result)

    if result == '':
        result = '1'
    return result


def the_poly(p,x,index):
    if p[index][0] == 0 and p[index][0] == 1:
        cap = ''
    else:
        cap = '^'

    if p[index][0] == 0 and p[index][0] == 1:
        var = ''
    else:
        var = x 

    tail = str(abs(p[index][1])) + var + cap + str(abs(p[index][0]))


    if p[index][0] > 1:
        if p[index][1] < 0:   
            if index == 0:
                if p[index][1] ==  -1:
                    ans = '-' + var + cap + str(abs(p[index][0]))
                else:
                    ans = '-' + tail
            else:
                if p[index][1] ==  -1:
                    ans = ' - ' + var + cap + str(abs(p[index][0]))
                else:
                    ans = ' - ' + tail


            
        elif p[index][1] > 0:
            if index == 0:
                if p[index][1] ==  1:
                    ans = var + cap + str(abs(p[index][0]))
                else:
                    ans = tail
            else:
                if p[index][1] ==  1:
                    ans = ' + ' + var + cap + str(abs(p[index][0]))
                else:
                    ans = ' + ' + tail
       
            

    elif p[index][0] == 0:
        if p[index][1] < 0:
            if index == 0:
                ans = '-' + str(abs(p[index][1])) 
            else:
                ans = ' - ' + str(abs(p[index][1]))  
            return ans
        elif p[index][1] > 0:
            if index == 0:
                ans = str(abs(p[index][1])) 
            else:
                ans = ' + ' + str(abs(p[index][1])) 



    elif p[index][0] == 1:
        if p[index][1] < 0:
            if index == 0:
                if p[index][1] ==  -1:
                    ans = '-' + var
                else:
                    ans = '-' + str(abs(p[index][1])) + var 
            else:
                if p[index][1] ==  -1:
                    ans = ' - ' + var
                else:
                    ans = ' - ' + str(abs(p[index][1])) + var 
                 
            return ans
        elif p[index][1] > 0:
            if index == 0:
                if p[index][1] == 1:
                    ans = var
                else: 
                    ans = str(p[index][1]) + var    
            else:
                if p[index][1] == 1:
                    ans = ' + ' + var
                else:
                    ans = ' + ' + str(abs(p[index][1])) + var

            return ans


    

    return ans ###########################################


    
    

def test():
    assert print_polynomial([(0,-1)], 'x') == "-1"
    assert print_polynomial([(1,-6)], 'x') == "-6x"
    assert print_polynomial([(1, 1)], 'x') == "x"
    assert print_polynomial([(2, 0), (1, -1)], 'x') == "-x"
    assert print_polynomial([(1, -1)], 'v') == "-v"
    assert print_polynomial([(2, -1)], "x") == "-x^2"
    assert print_polynomial([(191, 2)], "x") == "2x^191"
    assert print_polynomial([(0, 1), (2, 100)], 'x') == "100x^2 + 1"
    assert print_polynomial([(0, 1)], 'x') == "1"
    assert print_polynomial([(1, 0)], 'y') == "0"
    assert print_polynomial([(0, 0)], 'x') == "0"
    assert print_polynomial([(0, 0), (1, 0)], 'h') == "0"

    assert print_polynomial([(0, -6.5), (1, 0.1)], 'x') == "0.1x - 6.5"
    assert print_polynomial([(0, -6.5), (1, -0.1)], 'x') == "-0.1x - 6.5"
    assert print_polynomial([(0, -4), (1, 0.5)], "x") == "0.5x - 4"
    assert print_polynomial([(1, 0.5), (0, 2.3)], "x") == "0.5x + 2.3"

    assert print_polynomial([(1, -1), (0, -1)], 'x') == "-x - 1"
    assert print_polynomial([(1, 1), (0, -1)], 'y') == "y - 1"
    assert print_polynomial([(3, 0), (0, 1), (1, -1)], 'x') == "-x + 1"
    assert print_polynomial([(2, 34), (0, -1)], "y") == "34y^2 - 1"
    assert print_polynomial([(0, -15), (2, 1), (3, 0)], "x") == "x^2 - 15"
    assert print_polynomial([(3, 2), (0, 8), (1, -1)], "x") == "2x^3 - x + 8"
    assert print_polynomial([(3, -2), (0, 8), (1, 1)], "x") == "-2x^3 + x + 8"
    assert print_polynomial([(19, 1), (10, 2)], "x") == "x^19 + 2x^10"
    assert print_polynomial([(109, 1), (10, 2)], "x") == "x^109 + 2x^10"
    assert print_polynomial([(109, -1), (11, 1)], "x") == "-x^109 + x^11"
    assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'x') == "-6x^2 + 34x - 8"
    assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'y') == "-6y^2 + 34y - 8"
    assert print_polynomial([(2,6), (0,-8), (1,34)], 'x') == "6x^2 + 34x - 8"
    assert print_polynomial([(2,6), (0,-8), (1,34), (5, -21)], 'x') == "-21x^5 + 6x^2 + 34x - 8"
    assert print_polynomial([(100,6), (0,-8), (1,34), (5, -21)], 'x') == "6x^100 - 21x^5 + 34x - 8"

    print("my love")


if __name__ == '__main__':
    main()

    #if p[index][0] == 0 and p[index][1] == 1 and len(p) > 2 and index != len(p)-1 and index != 1:
    #     return ''
    # elif p[index][0] == 0 and p[index][1] == -1 and len(p) > 2 and index != len(p)-1 and index != 1:
    #     return ''

    # elif p[index][0] == 0 and p[index][1] == 1 and len(p) == 2 and index != len(p)-1:
    #     return '1'
    # elif p[index][0] == 0 and p[index][1] == -1 and len(p) == 2 and index != len(p)-1:
    #     return '1'
   
    # elif p[index][0] == 0 and p[index][1] == 1 and len(p) == 1:
    #     return '1'
    # elif p[index][0] == 0 and p[index][1] == -1 and len(p) == 1:
    #     return '1'

    
    
                
    # elif p[index][0] == 1 and p[index][1] == 1:
    #     return x
    # elif p[index][0] == 1 :
    #     return x
    # elif p[index][0] == 0 :
    #     return ''
    # else: return x + '^' + str(abs(p[index][0]))

