#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW13_1
# 204111 Sec 003
# TA-67 Tan

def main():
    assert product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00) \
    == {'stool': 0.3,'chair': 0.4,'pillow': 3.5}
    assert product_shopping({"chair": (0.4, 450.0), "pillow": (3.5, 315.0),"stool": (0.3, 300.0), "closet": (2.5, 700.0)}, 15.0,1450.00)\
    == {'stool': 0.3,'chair': 0.4,'closet': 2.5}
    assert product_shopping({"a":(0.1,10)},100.0,100.0) == {'a': 0.1}
    assert product_shopping({"a":(0.1,10)},100.0,1.0) == {}
    assert product_shopping({"shirt": (0.13, 1200.), "trousers": (0.36, 850.),"jeans": (0.3, 1300.), "shoes": (0.5, 1200.),"socks": (0.15, 50.)},5.0,4200.00)\
    == {'jeans': 0.3, 'shirt': 0.13, 'socks': 0.15, 'trousers': 0.36}
    assert product_shopping({'j': (43, 83), 'b': (68, 95), 'f': (35, 12), 'g': (45, 58), 'd': (75, 36), 'c': (18, 55), 'x': (92, 80), 'i': (84, 98), 'm': (55, 76), 'q': (78, 38), 'w': (1, 48), 'v': (34, 47), 'l': (0, 86)},67,96)\
    == {'w': 1, 'v': 34}
    print('kid tang nan -> kid mak pai')


def product_shopping(p_list: dict[str, tuple[float, float]], allowed_w: float, budget: float):

    power_set = [[]]
    for i in p_list:
        part = list(map(lambda x: x + [i],power_set))
        power_set.extend(part) 
    power_set = power_set[1:]

    solution = []
    for i in power_set:
        weight = []
        money = []
        solut = []
        for j in range(len(i)):
            weight += [p_list[i[j]][0]] 
            money += [p_list[i[j]][1]]
        weight = sum(weight)
        money = sum(money)
        solut.append([i, weight, money])
        solution.extend(solut)
  
    select = list(filter(lambda x: x[1] <= allowed_w and x[2] <= budget, solution))

    if select == []:
        result = {}
    else:
        max_obj = max(list(map(lambda x: len(x[0]),select)))
        only = list(filter(lambda x: len(x[0]) == max_obj, select))
        min_weight = min(list(map(lambda x: x[1], only)))
        answer = list(filter(lambda x: x[1] == min_weight, only))

        result = dict()
        for i in answer[0][0]:
            result[i] = p_list[i][0]
    return result


if __name__ =='__main__':
    main()