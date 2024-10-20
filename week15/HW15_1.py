#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Hw15_1
# 204111 Sec 003
# TA-66 Film

def main():
    # shelf = [('Bleach', 10), ('Naruto', 5), ('One Piece', 24)]
    # new = ('Naruto', 18)
    # manga_add(shelf, new, True)
    # print('--')
    # print(shelf)

    # shelf = [('Bleach', 100), ('Bleach', 10000)]
    # new = ('Bleach', 99)
    # manga_add(shelf, new, True)
    # print('--')
    # print(shelf)

    shelf = [('Bleach', 1), ('Bleach', 3), ('Bleach', 4)]
    new = ('Bleach', 2)
    manga_add(shelf, new, True)
    print('--')
    print(shelf)


def manga_add(manga_shelf: list[tuple[str, int]], new_m: tuple[str, int], show_steps: bool = False):
    if manga_shelf == [] :  

        manga_shelf.append(new_m) 

    else :  

        low = 0 

        hight = len(manga_shelf) - 1 

        # print(nearless)

        while low <= hight : 

            mid = (low + hight) // 2     

            if new_m == manga_shelf[mid] :   

                if show_steps == True : 

                    print(('[' + str(mid) + ']'), manga_shelf[mid])

                manga_shelf.insert(mid, new_m)   

                break    

            elif is_less_than(manga_shelf[mid], new_m) :  

                if show_steps == True : 

                    print(('[' + str(mid) + ']'), manga_shelf[mid])

                hight = mid - 1 

            elif is_more_than(manga_shelf[mid], new_m) :  

                if show_steps == True : 

                    print(('[' + str(mid) + ']'), manga_shelf[mid])

                low = mid + 1     

        if is_less_than(manga_shelf[mid], new_m) :  

            manga_shelf.insert(mid, new_m) 

        else :  

            manga_shelf.insert(mid + 1, new_m)             

def is_less_than(x, y) :  
    if x[0] == y[0] :  
        if y[1] < x[1]  :  
            return True 
        else : 
            return False 
    else :   
        if y[0] < x[0] :  
            return True 
        else :  
            return False  

def is_more_than(x, y) :  
    if x[0] == y[0] :  
        if y[1] > x[1]  : 
            return True 
        else : 
            return False 

    else :  
        if y[0] > x[0] :  
            return True 
        else :  
            return False       


if __name__ == '__main__':
    main()