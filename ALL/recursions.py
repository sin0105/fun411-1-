# หาจำนวนเฉพาะ

# def prime_factor(x):
# 	prime_factor_helper(x, 2)

# def prime_factor_helper(x, div): # helper func
# 	# base case
# 	if div > x ** 0.5:
# 		print(x)
# 		return
# 	# d & c
# 	if (x % div == 0):
# 		print(div, end=' ')
# 		prime_factor_helper(x // div, div)
# 	else:
# 		prime_factor_helper(x, div + 1)
# prime_factor(19)

####################################################################

# def tail(n):
# 	if (n == 0):
# 		return

# 	print(n,end =" ")

# 	tail(n-1)       # 5 -> 5 3 4 2
# tail(5)

# print('\n')

# def head(n):
# 	if (n == 0):
# 		return

# 	head(n-1)

# 	print(n,end =" ")
# head(5)

####################################################################

# # ดึงเลขออกมาแต่ลละหลัก      
# def dgt_print_h1(n): 
# 	if n == 0:
# 		return

# 	dgt_print_h1(n//10)
# 	print(n%10,end=" ")

# dgt_print_h1(3456)

# print('\n')


# def dgt_print_t1(n,div=None):
# 	if div is None:
# 		div = 10**(len(str(n))-1)

# 	if div < 1:
# 		return

# 	print(n//div,end=" ")
# 	dgt_print_t1(n%div,div//10)

# dgt_print_t1(3456)

# print('\n')

# # ดึงเลขออกมาแต่ละหลัก แบบย้อนหลัก

# def dgt_print_h2(n, div=None):
# 	if div is None:
# 		div = 10**(len(str(n))-1)
# 	if div < 1:
# 		return

# 	dgt_print_h2(n % div, div//10)
# 	print(n//div, end=" ")
# dgt_print_h2(567)

####################################################################

# def range_sum(lo, hi):
# 	if lo == hi:
# 		return lo

# 	head_sum = lo
# 	tail_sum = range_sum(lo+1,hi)

# 	return head_sum + tail_sum
# print(range_sum(10, 15))

###################################################################

# power
# def power(base, exp): # non-negative integer exp

# 	if exp == 0:
# 		return 1

# 	result_head = base
# 	result_tail = power(base,exp-1)

# 	return result_head * result_tail

# print(power(2, 5))

###################################################################
s = 'asxcv'
if 's' in s:
    hh = s.replace('s','')
    print(hh)
if 'x' in hh:
    hh = hh.replace('x','')
    print(hh)

   
























