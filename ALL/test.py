#(( 1 ))############################################################################(( 1 ))
# def main():
#     print(find_mode([1,2,3]))


# def find_mode(score_list:list[int]):
#     sort = sorted(score_list)
   
#     con = list(map(lambda x: sort.count(x),sort))
#     con_max = max(con)

#     tup = list(map(lambda x,y: (x,y),sort,con))
#     fill = list(filter(lambda x: x[1] == con_max,tup))

#     top,bot = zip(*fill)
#     top =list(top)
    
#     ste = list(filter(lambda x: x%con_max == 0,range(0,len(top))))
#     result = list(map(lambda y: top[y],ste))
#     return result


#(( 2 ))############################################################################(( 2 ))
# def main():
#     same_letters('abcde','bbcddAA')


# def same_letters(str1:str,str2:str):
#     str1 = str1.lower()
#     str1 = list(filter(lambda x: x.isalpha(),str1))
    
#     str2 = str2.lower()
#     str2 = list(filter(lambda x: x.isalpha(),str2))

#     bo1 = list(map(lambda x: x in str2,str1))
#     bo2 = list(map(lambda x: x in str1,str2))

#     all_bool = all(bo1 + bo2)
#     return all_bool



#(( 3/6 ))############################################################################(( 3/6 ))
# def main():
#     count_lucky_num(1,14)


# def count_lucky_num(start:int,stop:int):
#     alll = list(filter(lambda x: x % 7 == 0,range(start,stop)))
#     result = len(list(filter(lambda x: str(7) not in str(x), alll)))
#     return result

#(( 4/6 ))############################################################################(( 4/6 ))
# from functools import reduce

# def main():
#     find_min([1, 0, 2, 3])


# def find_min(list_a:list[int]):
#     result =  reduce(lambda x,y: x if x < y else y, list_a)
#     return result
#(( 6/6 ))############################################################################(( 5/6 ))
# def main():
#     median([1,2,3])


# def median(list_a:list[int]):
#     lenn = len(list_a)//2
#     if len(list_a) % 2 == 1:
#         return list_a[lenn]
#     elif len(list_a) % 2 == 0:
#         return (list_a[lenn-1] + list_a[lenn])/2


#(( 6/6 ))############################################################################(( 6/6 ))
# def main():
#     adjacent_sum([0, 1, 2])


# def adjacent_sum(list_a:list[int]):
#     summer = list(map(lambda x: list_a[x] + list_a[x+1],range(0,len(list_a)-1)))
#     return summer

# if __name__ == '__main__':
#     main()

'''
from functools import reduce
def main():
    good([2,8,1])

def good(list_):
    print(list_)
    jj = list(map(lambda x: list_[:x],range(1,len(list_)+1)))
    print(jj)
    ss = list(map(lambda x: sorted(x),jj))
    print(ss)

    dd = list(map(lambda x: ss[x][-1],range(0,len(list_)-1)))
    print(dd)

    ff = [max(list_)]
    print(ff)

    cc = dd + ff
    print(cc)


if __name__ == '__main__':
    main()
'''
 

