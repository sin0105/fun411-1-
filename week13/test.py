# ----------------------------------------( 1 )
# def main():
#     # print(matrix_mult([[1, 2, 3], [4, 5, 6]] ,[[7, 8], [9, 10], [11,12]]))
#     print(matrix_mult([[1, 2, 3], [4, 5, 6]] ,[[7, 8, 5, 9, 3], [9, 10, -3, 7, 13], [11, 12, 6, 2, 9]]))

# def matrix_mult(m1: list[list[int]], m2: list[list[int]]):
#     if len(m1) == 0 or len(m2) == 0 or len(m1[0]) != len(m2):
#         return None


#     find_all = []
#     for i in range(len(m1)): #2 0,1
#         for j in range(len(m2[0])):# 0,1
#             for k in range(len(m2)):# 0,1,2
#                 find_all.append(m1[i][k] * m2[k][j])
#     # [7, 18, 33, 8, 20, 36, 28, 45, 66, 32, 50, 72]

#     solu = list(map(lambda x: sum(find_all[x*len(m1[0]) : (x*len(m1[0]))+len(m1[0])]), range(len(find_all)//len(m1[0]))))
#     print(solu)

#     result = []
#     for i in range(len(m1)):
#         result.append(solu[i*len(m2[0]) : i*len(m2[0])+len(m2[0])])
#     return result

# ----------------------------------------( 2 )
# def main():
#     square_matrix([[1, 2], [1, 2, 3, 2, 3, 2, 1, 3], [1, 2], [1, 2], [1]])
#     square_matrix([[2, 3, 4], [1, 2, 3]])
    
    
# def square_matrix(list_x: list[list[int]]):
#     colum = max(map(lambda x: len(x),list_x)) 
#     row = len(list_x)
#     maxx = max([colum, row])

#     minus = []
#     for i in list_x:
#         minus.append(maxx - len(i))
    
#     zero = []
#     for i in minus:
#         zero.append([0]*i)
    
#     result1 = []
#     for i in range(len(list_x)):
#         result1.append(list_x[i] + zero[i])
    
#     result2 = []
#     if colum > row:
#         for i in range(colum - row):
#             result2.append([0]*colum)

#     list_x[:] = result1 + result2
#     print(list_x)
    
# ----------------------------------------( 3 )
# def main():
#     print(product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00))


# def product_shopping(p_list: dict[str, tuple[float, float]], allowed_w: float, budget: float):
#     power_set = [[]]
#     for i in p_list:
#         part = list(map(lambda x: x + [i],power_set))
#         power_set.extend(part) 
#     power_set = power_set[1:]

#     solution = []
#     for i in power_set:
#         weight = []
#         money = []
#         solut = []
#         for j in range(len(i)):
#             weight += [p_list[i[j]][0]]
#             money += [p_list[i[j]][1]]
#         weight = sum(weight)
#         money = sum(money)
#         solut.append([i, weight, money])
#         solution.extend(solut)

#     select = list(filter(lambda x: x[1] <= allowed_w and x[2] <= budget, solution))

#     if select == []:
#         dic = {}
#     else:
#         max_shop = max(map(lambda x: len(x[0]),select))
#         shop_select = list(filter(lambda x: len(x[0]) == max_shop, select))
#         min_weight = min(map(lambda x: x[1], shop_select))
#         weight_select = list(filter(lambda x: x[1] == min_weight, shop_select))[0][0]
        
#     dic = dict()
#     for i in weight_select:
#         dic[i] = p_list[i][0]
#     return dic

# ----------------------------------------( 4 )
# def main():
#     print(count_vote([['Mewtwo', 'Pikachu', 'Suicune'],
#                     ['Mewtwo', 'Suicune', 'Pikachu'],
#                     ['Pikachu', 'Rayquaza', 'Charizard'],
#                     ['Suicune', 'Pikachu', 'Charizard']]))

# def count_vote(pref_matrix: list[list[str]]):
#     plus = list(map(lambda x: ['1'] + x, pref_matrix[::-1]))

#     char = tuple()
#     for i in pref_matrix:
#         char += tuple(i)
#     char = list(set(char))

#     dic = dict()
#     for i in plus:
#         for j in range(len(i)):
#             dic[i[j]] = j + dic.get(i[j],0)

#     sort = sorted(map(lambda x: (x, dic[x]), char))
#     result = sorted(sort, key=lambda x: x[1], reverse=True)
#     return result

# ----------------------------------------( 5 )
def main():
    print(sum_d_product([[3, 3, 3, 2], [2, 0, 3, 1], [2, 1, 2, 3], [1, 0, 2, -1]]))

def sum_d_product(m: list[list[int]]):
    if len(m) == 2:
        result = (m[0][0] * m[1][1]) + (m[0][1] * m[1][0])
        return result

    ans = []
    for i in range(0,len(m),2):
        skip1 = range(0,len(m),2)
        skip2 = range(1,len(m),2)
        solution = list(map(lambda x,y: (m[i][x] * m[i+1][y]) +  (m[i][y] * m[i+1][x]), skip1, skip2))
        ans.extend([solution])

    result = sum_d_product(ans)
    return result


if __name__ == '__main__':
    main()