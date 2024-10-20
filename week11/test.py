DEBUG = True
# def powerset(set_a: set[int]):
#     a = [set()]
#     for i in set_a:
#         with_num = list(map(lambda x: x | {i},a))
#         a += with_num
#     # print(a)
#     # print(a in [set(),{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}])   
#     check =  [set(),{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}]
#     check_1 = list(map(lambda x: x in check,a))
#     if DEBUG:
#         print(check_1)
#         print(a)
#     return a
    
    
def powerset(set_a):
    a = [()]
    for i in set_a:
        b = list(map(lambda x: x + (i,),a))
        a += b 
    return a

def arrive(l,r,result = ()):
    if len(l) == 0:
        result += r
        result = '>'.join(result)
        return (result,)
    if len(r) == 0:
        result += l
        result = '>'.join(result)
        return (result,)

    left = arrive(l[1:],r,result + (l[0],))
    right = arrive(l,r[1:],result + (r[0],))

    solution = left + right 
    pritn('solution : ',solution)
    return solution




def all_bus(set_a):
    so1 = powerset(set_a)[1:-1]
    
    if DEBUG: print('s1 : ',so1)
    so2 = []
    for i,s2 in enumerate(reversed(so1)):
        so2.append(s2,)
    if DEBUG: print('s2 : ',so2)
    
    zip_solu = list(zip(so1,so2))
    if DEBUG: print('zip1 : ',zip_solu)

    # result = sorted(set(map(lambda x: x[0] + x[1],zip_solu)))
    # if DEBUG: print('result : ',(result))
    result = set()
    for i in zip_solu:
        result.update(set(arrive(i[0],i[1])))
    print(sorted(result))
    return result


                                           
             

if __name__ == '__main__':
    all_bus([1, 2, 3])
    # arrive((1,), (2, 3))
    print(powerset([1, 2, 3]))

    # assert powerset({1, 2, 3}) in [set(),{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}]
    # result = [set(),{1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}]
    # assert list(map(lambda x: x in result, powerset({1, 2, 3})))
    # print('all ok')


