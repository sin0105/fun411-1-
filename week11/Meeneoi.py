#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# EX11
# 204111 Sec 003


def main():
    test()
    print(eeny_meeny(['John', 'Ann', 'Tom'], 2))


def eeny_meeny(name_list: list[str], rhyme_len: int=4):
    text = ''.join(name_list)
    dic = {}
    re = 0

    index_big = list(filter(lambda x: text[x].isupper(),range(len(text))))
    dic = dict(map(lambda x: (index_big[x], name_list[x]),range(len(index_big))))
    # {0: 'Jhon', 4: 'Ann', 7: Tom}

    i = 0
    roundd = 0
    up = len(name_list) # (3)

    while up != 1: # ตัวใหญ่เท่ากับ 1 ให้หยุด
        #   (0)<----| ((i + 1) % len(text)) % ลงตัวเป็น 0
        # -> ###Abc-| พอทำครบ i จะเป็น 0 ซึ่งเป็นการวนไปนับ index ใหม่ <------------------------|
        #                                                                                 |
        if text[i] == '#':  # ไล่ index ไปเรื่อยๆจนกว่าจะหลุด #                                |
            i = ((i + 1) % len(text)) # i เพิ่มขึ้น แต่จะไม่มากกว่า ความยาว text (i +=1)         |
            continue#                                                                     |
        roundd += 1         # พอหลุดแล้วให้ round เพิ่ม1 คือการนับ  # -> ###A(r.1) b(r.2) c(r.3)-|
        if roundd == rhyme_len:     #   พอ round = ตัวอักษรที่ต้องเลือก ส่งไปเช็ค เล็ก ใหญ่
            if i not in index_big:  
                text = text[:i] + '#' + text[i+1:]  # ตัวเล็ก (#) แทรก
            elif i in index_big:
                text = text[:i] + '#'*len(dic[i]) + text[i+len(dic[i]):] # ตัวใหญ่ (#) คูณจน.len(ใหญ่)->dic 
                up -= 1 # ลดค่า up ซึ่งแทนตัวใหญ่
            roundd = 0  # ผ่านเงื่องไขให้ reset round และเริ่มนับ roundใหม่
        i = ((i + 1) % len(text)) 

    result = list(filter(lambda x: text[x].isupper(),range(0,len(text)))) # พอเหลือใหญ่ 1 ตัว เราจะเอา ใหญ่มาเข้า dic
    result = dic[result[0]]
    return result

def test():
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['John', 'Ann', 'Tom'], 5) == 'Tom'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(['Ann', 'John', 'Meen-eoi']) == 'Ann'
    assert eeny_meeny(['John', 'Ann', 'Tom'], 2) == 'John'
    print('ko rong')

if __name__ == '__main__':
    main()
        
     


    # people = text
    # for i in range(len(text)+1):
    #     print(i, people[i], people)  
    #     if i % rhyme_len == 0:
    #         if text[i].islower():
    #             people = people[:i] + people[i+1:]
                
    #         elif text[i].isupper():
    #             people = people[:i] + people[i+dic[people[i]]:]
           
    # print(people)


    # people = ''
    # for i,word in enumerate(text):
    #     if i % rhyme_len == 0:
    #         if word.islower():
    #             people += text[:i] + text[i+1:]

    #         # if word.isupper():
    #         #     people += text[:i] + text[i+dic[word]:]
    # print(people)

