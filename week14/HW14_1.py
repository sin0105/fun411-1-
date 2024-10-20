#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Hw14_1
# 204111 Sec 003
# TA-66 Film , TA-67 Ton, TA-67 Tan

def main():
    append_ranking()

def append_ranking(infile_name: str='score_in.txt', outfile_name: str='score_out.txt'):

    with open(infile_name, "rt") as infile:
        zero = []
        alll = []
        for line in infile:
            alll.append(line.strip('\n').replace('None','0'))
            zero.append(line.strip('\n'))
               
        summ = []
        for i in alll:
            find = (i.split())
            first = sorted(map(float,find[1:]))
            
            sec = sum(first[1:])
            summ.append((find[0],sec))
        
        reverse = ['<3'] + sorted(summ,key = lambda x:x[1],reverse = True)


        keep = []
        for i in range(len(reverse)):
            keep.append((reverse[i][0],i))
        keep = keep[1:]

        dic = dict()
        for i in keep:
            dic[i[0]] = i[1]

        select = list(map(lambda x: x[:9],alll))
        fill = list(map(lambda x,y: x + ' ' + str(dic[y]),zero,select))
                 
        with open(outfile_name, "wt") as outfile:
                outfile.write('\n'.join(fill))
                    

if __name__ == '__main__':
    main()