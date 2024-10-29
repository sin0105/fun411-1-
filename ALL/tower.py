def main():
    print(cell_coverage([(1, 1, 1), (0, 0, 1)], 2, 4))


def cell_coverage(tower_list, area1, area2):
    tower_list = set(tower_list)
    result = set()
    dic = dict()
    for tower in tower_list:
        for i in range(tower[0]+tower[2]+1):
            for j in range(tower[1]+tower[2]+1):
                alll = (i,j)
                if cal(tower, alll[0], alll[1]) <= tower[2] and i < area1 and j < area2:
                    result.add(alll)
        result.remove((tower[0],tower[1]))
        dic[(tower[0], tower[1])] = result
        result = set()
    return dic
    

def cal(tower, x, y):
    distance = (((tower[0]-x)**2) +  ((tower[1]-y)**2))**0.5
    return distance


if __name__ == '__main__':
    main()