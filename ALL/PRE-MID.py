#( 1 ) #################################################################
# def main():
#     test()

# def is_right_triangle(a, b, c):
#     num = sorted([a,b,c])
#     aa = num[2]**2
#     bb = num[0]**2
#     cc = num[1]**2
#     if aa == bb+cc:
#         return True
#     else:
#         return False
#     return aa == bb+cc reสั้นๆ
    
# def test():
#     assert is_right_triangle(3,4,5) is True
#     assert is_right_triangle(5,3,4) is True
#     assert is_right_triangle(5,12,13) is True
#     assert is_right_triangle(3,13,13) is False
#     print("LOVE FILM")


# if __name__ == '__main__':
#     main()

#( 2 ) #################################################################
# def main():
#     # print(transform_id(624545555911))

# def transform_id(int_id):
#     return str(int_id)[-3:] + '-' + str(int_id)[:2]


# if __name__ == '__main__':
#     main()

#( 3 ) #################################################################
# def main():
#    count_4n5(154)

# def count_4n5(n):
#     return len(list(filter(lambda x: str(4) in str(x) and str(5) in str(x),range(0,n+1))))
  

# if __name__ == '__main__':
#     main()

#( 4 ) #################################################################
# from math import isclose
# from math import log2


# def log2_list(list_a):
#     list_a[:] = (list(map(lambda x: log2(list_a[x]),range(0,len(list_a)))))



# if __name__ == '__main__':

#     list_a = [1, 2, 4]
#     log2_list(list_a)
#     assert all(map(lambda x, y: isclose(x, y, abs_tol=0.001),
#                    list_a, [0.0, 1.0, 2.0]))

#     print("All OK!")

#( 5 ) #################################################################
# def main():
#     (reverse_cap(['I', 'bought', 'two', 'bananas']))

# def reverse_cap(list_a):
#     return list(map(lambda x: list_a[x][0].lower()+list_a[x][1:].upper(),range(0,len(list_a))))

# if __name__ == '__main__':
#     main()

#( 6 ) #################################################################
# from math import isclose


# def harmonic_mean(list_a):
#     return len(list_a)/sum(list(map(lambda x: 1/list_a[x],range(0,len(list_a)))))
   


# if __name__ == '__main__':
#     assert isclose(harmonic_mean([1, 2, 2, 2]), 1.6, abs_tol=0.001)

#     print("All OK!")
