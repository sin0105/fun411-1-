import string
def main():
    # people = [('Tan' ,650), ('Ton',600), ('Aom', 400), ('Noon', 500) ,('Ice',600), ('Toey', 550)]
    people = [('Tan' ,600), ('Ton',600), ('Aom', 400), ('Noon', 500) ,('Ice',600), ('Toey', 500)]

    # people = []
    # people = [('Film' ,650)]
    result = sort(people, show_steps = True)
    print('---')
    print(result)

def sort(over_all,show_steps = False):
    if over_all == []: return []

    dic = {x: [] for x in ' ' + string.ascii_uppercase + string.ascii_lowercase }
    name = dict(over_all) 
    maxx = max(list(map(lambda x: len(x[0]),over_all)))

    plus = []
    for k in over_all:
        plus.append(k[0] +  (maxx - len(k[0]))*' ')
    
    for i in range(-maxx,0)[::-1]:
        for j in plus:
            dic[j[i]] += [j]

        plus = []
        for k in dic.values():
            plus += k
        dic = {x: [] for x in ' ' + string.ascii_uppercase + string.ascii_lowercase}
        show = list(map(lambda x: (x.strip(), name[x.strip()]),plus)) 
        if show_steps == True: print(show)

#-----------------------------------------------------------------------------------------------------#

    for i in range(1,len(show)):
        j = i
        while j > 0 and show[j][1] > show[j-1][1]:
            show[j], show[j-1] = show[j-1], show[j]
            j -= 1
        if show_steps == True: print(show)



    keep = 1
    result = []
    for i in range(len(show)):
        for j in range(len(show)):
            if show[i][1] < show[j][1] and i != j:
                keep += 1
        result.append(keep)
        keep = 1

    result = list(map(lambda x: show[x]+(result[x],),range(len(result))))
    return result


if __name__ == '__main__':
    main()
