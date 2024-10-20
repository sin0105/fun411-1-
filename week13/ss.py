def main():
    print(sand_towers([10,10,9,10,6]))


def sand_towers(list_a: list[int]):
    
    a = '    |>>~ '
    b = '    |    '
    c = '  /^^^\\  '
    d = ' /     \\ '
    e = '/^^^^^^^\\'
    maxi = max(list_a) #10

    part = []
    all_p = []
    under = []
    ans = []
    for i in list_a:#[10,10,8,7,6]
        if i != maxi:
            k = maxi - i
            zero = ' '*((i*2)+1)
            for s in range(k+2):
                all_p += [zero]

        if i == maxi:
            for k in [a,b]:
                all_p.append((' '*(i-4)) + k + (' '*(i-4)))

        for j in [c,d,e]:
            all_p.append((' '*(i-4)) + j + (' '*(i-4)))
        
        for mid in range(1,i-3):
            all_p.append(' '*(abs((i-1)-mid-3)) + '/' + ' '*(7+(2*mid)) + '\\' + ' '*(abs((i-1)-mid-3)))
        
        part.append(all_p)
        all_p = []
        under += ['/' + ':'*(i*2)]

    dd = ''
    zz =[]
    for i in range(len(part[0])):
      for j in range(len(part)):
        if j == 0 :
          dd += ' ' +part[j][i]
        else:
          dd += part[j][i]
      zz.append(dd)
      dd = ''


    solut = '\n'.join(zz)
    under = ''.join(under) +':\\'
    result = solut + '\n' + under
    return '\n' + result









if __name__ == '__main__':
    main()