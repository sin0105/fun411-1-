# (d: decimal, b: binary, f: float)
# for i in range(1,5):
#     print('i = {0:b}'.format(i))
#############################################

# a = [1,2,3,4,5,6,7,8,8]
# for i in range(2,len(a),2):
#     print('a = ',a[i])

# for i in range(2,8,-2):
#     print('i = {0:d}'.format(i))

############################################

# def derivative(f,x):
#     h = 10**-8
#     return (f(x+h) - f(x))/h 

# def f(x):
#     return 4*x + 3

# print(derivative(f,2))

# def g(x):
#     return 4*x**2+3
# print(derivative(g,2))

############################################

# def longest_word(*args):
#     # print(args)
#     if (len(args) == 0):
#         return None 
#     result = args[0]
#     for word in args:
#         if (len(word) > len(result)):
#             result = word 
#     return result
# print(longest_word("this", "is", "really", "nice")) # really

# mywords = ["this", "is", "really", "nice"] 
# print(longest_word(mywords))
# # ['this', 'is', 'really', 'nice’]
# print(longest_word(*mywords)) # really

############################################

# def score_average():

#     SENTINEL = -1
#     print("Please enter students' score one for each line") 
#     print("and %d for termination: " % SENTINEL)
#     total = 0.0
#     count = 0
#     while (True):
#         score = float(input(""))
#         if score == SENTINEL: break
#         total += score 
#         count += 1
#     if count > 0: 
#         average = total / count
#     else: average = 0
#     print("The average of the %d numbers is %8.4f" %(count, average))

# score_average()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# def insert_comma_manual(number, position):
 
#   number_str = str(number)
#   result = ""
#   for i, digit in enumerate(reversed(number_str)):
#     if i % position == 0 and i != 0:
#       result = digit + "," + result
#     else:
#       result = digit + result
#   return result


# print(insert_comma_manual(123453454565,2))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# a = [90,93]
# v = [93]
# f = []


# print((a+v).count(max(a+v)))

# print((a+v+f).count(max(a+v+f)))

# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter: 
#             return index
#         index = index + 1 
#     return -1

# print(find('abc','b'))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# def merge_list(list_a, list_b):

#     len_a = len(list_a) 
#     len_b = len(list_b) 
#     i=0
#     j=0
#     list_c = []

#     while i < len_a and j < len_b: 
#         if list_a[i] < list_b[j]:
#             list_c.append(list_a[i])
#             i += 1
#         else: 
#             list_c.append(list_b[j]) 
#             j += 1
#     if i < len_a: 
#         return list_c
#     if j < len_b: 
#         return list_c + list_b[j:]
#     return list_c

# print(merge_list([1, 3, 4, 5, 6],[2, 5, 7, 9, 10]))
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

