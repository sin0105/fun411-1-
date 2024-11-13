# TA Aom-67
#-------------------------------------------( 1 )
# import math
# a = float(input('a: '))
# b = float(input('b: '))
# c = float(input('c: '))

# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print('area:',math.ceil(area))

#-------------------------------------------( 2 )
# time = int(input('Input milliseconds: '))

# d = time // 86400000
# day = time % 86400000

# h = day // 3600000
# hour = day % 3600000

# m = hour // 60000
# minn = hour % 60000

# s = minn // 1000
# sec = minn % 1000

# mil = sec % 1000

# print(d, 'day(s),' ,h, 'hour(s),' ,m, 'minute(s),' ,s, 'second(s), and' ,mil, 'millisec(s)')

#-------------------------------------------( 3 )
# m1 = float(input('m1:' ))
# b1 = float(input('b1:' ))
# m2 = float(input('m2:' ))
# b2 = float(input('b2:' ))

# x = m1-m2
# b = b2-b1
# x = b/x

# y = (m1*x)+b1
# print('Lines intersect at (%.2f,%.2f)'%(x,y))

#-------------------------------------------( 4 )
x = int(input('x: '))
y = int(input('y: '))
x = x-1

part1 = int((y*(y+1))/2)
part2 = int((x*(x+1))/2)

summ = part1-part2
print('sum is:',summ)





