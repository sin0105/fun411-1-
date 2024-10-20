#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab08_2
# 204111 Sec 003

def main():
	test()

def reverse_digits(x: int):
	if x < 0:
		return reverse_digits_helper(x)*-1
	else:
		return reverse_digits_helper(x)
	
def reverse_digits_helper(n,div=None):
	n = abs(n)
	if div is None:
		div = 10**(len(str(n))-1)

	# base case	
	if div <= 1:
		return n

	# head + tail
	return reverse_digits_helper(n%div,div//10)*10 + n//div


def test():
	print(reverse_digits(-1234))
	assert reverse_digits(1234) == 4321
	assert reverse_digits(-1234) == -4321
	assert reverse_digits(1) == 1


	print("ALL OK BROTHER")

if __name__ == '__main__':
	main()
