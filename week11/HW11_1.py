#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW11_1
# 204111 Sec 003
# TA 66-Film


def main():
    test()
    # print(words_to_num('forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two'))

def words_to_num(words: str):
    num_dic = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
               "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15 ,
               "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, 
               "thirty": 30 ,"forty": 40, "fifty": 50 ,"sixty": 60, "seventy": 70, "eighty": 80, "ninety":90,
               "billion": 10**9, "million": 10**6, "thousand": 10**3, "hundred": 10**2}
    words = words.replace('-',' ')
    text = words.split()
    num_list = list(map(lambda x: num_dic[x],text))
   
    bil = 0
    mil = 0
    tho = 0
    hun = 0
    digit = 0

    for item in num_list:
        if item < 100:
            digit += item
        if item == 100:
            hun =  digit * 100
            digit = 0
        if item == 10**3:
            tho = (hun + digit) * 10**3
            hun, digit = 0, 0 # เอาอะไรเข้า รีเซตตัวนั้น                          
        if item  == 10**6:
            mil = (tho + hun + digit) * 10**6
            tho, hun, digit = 0, 0, 0
        if item == 10**9:
            bil = (tho + hun + digit) * 10**9
            tho, hun, digit = 0, 0, 0

    result = bil + mil + tho + hun + digit
    return result

def test():
    assert words_to_num('fourteen') == 14
    assert words_to_num('two hundred forty-eight') == 248
    assert words_to_num('one hundred eleven') == 111
    assert words_to_num('forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two') == 42641323862
    print('ko non')

if __name__ =='__main__':
    main()














# def find_index(n_list):
#     if 10**9 in n_list and 10**6 in n_list:
#         index = [n_list.index(10**9), n_list.index(10**6)]
#     elif 10**9 in n_list:
#         index = [n_list.index(10**9)]
#     elif 10**6 in n_list:
#         index = [-1, n_list.index(10**6)]
#     else:
#         index = []
#     return index


    # the_digit = num_list

    # for i, num in enumerate(the_digit):
    #     if num == 10**9:
    #         bil.extend(the_digit[:index[0]])
    #         print('b ',bil)

    #     if num == 10**6:
    #         mil.extend(the_digit[index[0]+1 : index[1]])
    #         print('m ',mil)

    #     if num == 10**3:
    #         tho.extend(the_digit[index[1]+1:])
    #         print('t ',tho)
           

        # if num == 10**2:
        #     hun.extend(the_digit[:i])
        #     print('h ',hun)
            
   


    # bil = []
    # mil = []
    # tho = []
    # hun = []
    # the_digit = num_list
    # the_digit2 = num_list[:]
    # for i, num in enumerate(the_digit):
    #     if num == 10**9:
    #         bil.extend(the_digit2[:i])
    #         the_digit2 = the_digit2[i+1:]
    #         print(the_digit)
    #         print(bil)
    #     for i, num in enumerate(bil):
    #         if num == 10**3:
    #             tho_b.extend(bil[:i])
    #             the_digit_b = bil[i+1:]
    #         print(the_digit)
    #         print(bil)
            
            

    #     if num == 10**6:
    #         mil.extend(the_digit2[:i])
    #         the_digit2 = the_digit2[i+1:]
    #         print(mil)
            

    #     if num == 10**3:
    #         tho.extend(the_digit[:i])
    #         the_digit = the_digit[i+1:]
           

    #     if num == 10**2:
    #         hun.extend(the_digit[:i])
    #         the_digit = the_digit[i+1:]
            



    # in_hun = num_list.index(100)
    # print(in_hun)

    # index = []
    # for i, num in enumerate(num_list):
    #     if num == 100:
    #         hun = num_list[i-1]
    #         hun_tail = sum(num_list[i+1:])
    #     
    #     # if num == 10**3:
    #     #     index.append(i)
    #     # if num == 10**6:
    #     #     index.append(i)

    # num_hun = (hun * 100) + hun_tail
    # print(num_hun)
    


