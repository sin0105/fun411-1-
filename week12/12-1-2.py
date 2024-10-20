print('(v1)*************************************************************************************(v1)')
'''
1
12
123
1234
12345
'''
size = 5
for i in range(size):
    for j in range(i+1):
        print(j + 1,end='')
    print('')
print('________________________________(1)')
'''
12345
1234
123
12
1
'''
size = 5
for i in range(size):
    for j in range(size - i):
        print(j + 1,end='')
    print('')
print('________________________________(2)')
'''
     *
    * *
   * * *
  * * * *
 * * * * *
 '''
size = 5
for i in range(size):
    for j in range(size - i):
        print(' ',end='')
    for k in range(i + 1):
        print('* ',end='')
    print('')
print('_________________________________(3)')
'''
7
-8
6
0
-4
possitive =  13.0
negative =  -12.0
'''
def pos_neg():
    pos = 0
    neg = 0
    # roundd = 5
    # for i in range(roundd):
        # x = float(input(''))
    num = [7, -8, 6, 0, -4]
    for x in num: 
        if x < 0:
            neg += x
        if x > 0:
            pos += x
    print('possitive = ',pos)
    print('negative = ',neg)
pos_neg()
print('_________________________________(4)')
# month is 4
def verify_month():
    while True:
        # month = int(input('enter (1-12): '))
        month = 4
        if month >=1 and month <=12:
            print('month is : ',month)
        else: print("Error - invalid month.")
        break
verify_month()
print('_________________________________(5)')
'''
Number sqare cube
------------------
  1       1      1
  2       4      8
  3       9     27
  4      16     64
  5      25    125
'''
def sqare():
    finall = 5
    print('Number sqare cube \n------------------')
    for num in range(1,finall+1):
        print('%3d %7d %6d'%(num, num**2, num**3))
sqare()
print('_________________________________(6)')

def equation(start, end):
    print('x value | y value \n-------- --------')
    x = start
    while x <= end:
        y = 10 * (x ** 2) + 3 * x - 2
        print("%6.2f %9.2f" % (x, y))
        x += 0.5
equation(4,6)
print('_________________________________(7)')
print('\n')


print('(v2)*************************************************************************************(v2)')
'''
(1)
i = 1
j = 1j = 2j = 3j = 4
i = 2
j = 1j = 2j = 3j = 4
i = 3
j = 1j = 2j = 3j = 4
i = 4
j = 1j = 2j = 3j = 4
i = 5
j = 1j = 2j = 3j = 4
'''

def nestedloop_helper(column):
    for j in range(1, column+1):
        print('j = %d' % j, end='')

def nestedloop():
    row = 5                     # ทำ 5 ครั้ง
    column = 4                  # สิ่งที่อยู่ในแต่ละครั้ง
    for i in range(1, row+1):
        print('\ni = %d' % i)

        nestedloop_helper(column)
print(nestedloop())
print('_______________________________________(1)')

'''
(2)
sum of week (1) = 32.000000
sum of week (2) = 48.000000
sum of week (3) = 121.000000
sum of week (4) = 160.000000
sum for all = 361.00
'''
def nestedloop_v2():
    week = 4
    day = 7
    week_total = 0
    all_total = 0
    sale = [(1,2,4,5,6,7,7),(8,9,9,5,4,6,7),(9,9,5,3,44,45,6),(57,77,3,4,5,6,8)]
    for i in range(week):
        for j in range(day):
        # sale = float(input(''))
            week_total += sale[i][j]
        all_total += week_total
        print('sum of week (%d) = %2f' % (i+1,week_total))
        week_total = 0 
    print('sum for all = %.2f' % (all_total))

nestedloop_v2()
print('_______________________________________(2)')
'''
     * * * * *
    * * * *
   * * *
  * *
 *
ใช้ i ซ้อนกัน
 '''
size = 5
for i in range(size):
    for i in range(size-i):
        print(' ',end='')

    for j in range(i + 1):
        print('* ',end='')
    print('')
print('_______________________________________(3)')
num2 = 7
for i in range(2,num2+1):
    if num2 % i == 0:
        break
if i != num2-1:
    print("%d divides %d" % (i, num2))
print('_______________________________________(4)')












