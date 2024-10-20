#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab_1
# 204111 Sec 003
# TA 66-Film

def main():
    print(word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."))
    print(word_count('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~1 \n555\n 0!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    print(word_count("\\Her/^__"))

def word_count(text: str):
    text = text.lower().split() # แยกคำด้วยช่องว่าง
    word = list(map(lambda x: x.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'),text)) # เอาตัวขอบออกทั้ง 2 ด้าน

    keep = dict()
    for item in word:
        count = 1 +  keep.get(item,0)  # count เก็บตัวซ้ำ
        keep[item] = count
    return keep

if __name__ == '__main__':
    main()
