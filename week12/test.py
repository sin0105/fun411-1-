DEBUG = False

def main():
    # test()
    print(scramble('123'))


def scramble(word):
    if len(word) == 1:
        return set(word)

    head = word[0]
    tail = word[1:]

    result = set()
    word_head = set()
    word_tail = scramble(tail)
    for i in word_tail:
        for j in range(len(i)+1):
           result |= {i[:j] + head + i[j:]}

    result = set(result) 
    print(len(result)) 
    result = list(result)
    return result
        


    
    

if __name__ == '__main__':
    main()    