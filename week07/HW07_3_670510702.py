#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW07_3
# 204111 Sec 003

def main():
	# test()
	print(num_to_word(13))

def three_digits_to_word(n: int):
	if n == 0: return ''            # คืนค่าว่าง
	hun,ten01 = divmod(n,100)		# divmod แยกหลัก
	ten,digit = divmod(ten01,10)
	digit_list = ["", "one", "two", "three", "four", "five","six", "seven", "eight", "nine", "ten",
				"eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
	ten_list = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety",]
	hun_list = ["","one hundred", "two hundred", "three hundred", "four hundred", "five hundred",
 				   "six hundred", "seven hundred", "eight hundred", "nine hundred"] 

	if n > 0 and n < 20:											# เคสเรียงเลขปกติ < 20
		return digit_list[n]

	if n > 19 and n < 100:											# เคสเรียงเลขปกติ < 100
		if digit == 0:												# 20 30 40 ...
			return ten_list[ten]
		else: return ten_list[ten] + '-' + digit_list[digit]		# มี - ต่อท้าย
		
	if n > 99 and n < 1000:											# เคสเรียงเลขปกติ < 1000
		if ten01 > 0 and ten01 < 20:								# 11 12 13 ...
			return hun_list[hun] + ' ' + digit_list[ten01]
		elif digit == 0:
			return hun_list[hun] + ' ' + ten_list[ten]
		else: return hun_list[hun] + ' ' + ten_list[ten] + '-'+ digit_list[digit]


def num_to_word(num: int):
	if num == 0: return 'zero'		# คืนค่า 0
	p_3,p4 = divmod(num,1000)		# divmod แยกหลัก
	p_2,p3 = divmod(p_3,1000)
	p1,p2 = divmod(p_2,1000)

	if p1 == 0:
		mark1 = ''					# คืนค่าว่าง เมื่อที่ตำแหน่ง p ใดๆเป็น 0
	else: mark1 = ' billion '		# คืนค่า หลัก
	if p2 == 0:
		mark2 = ''
	else: mark2 = ' million '
	if p3 == 0:
		mark3 = ''
	else: mark3 = ' thousand '
	
	result = three_digits_to_word(p1) + mark1 + \
			 three_digits_to_word(p2) + mark2 + \
			 three_digits_to_word(p3) + mark3 + \
			 three_digits_to_word(p4)
	return result

# def test():
# 	assert num_to_word(14) == 'fourteen'
# 	assert num_to_word(248) == 'two hundred forty-eight'
# 	assert num_to_word(111) == 'one hundred eleven'
# 	assert num_to_word(0) == 'zero'
# 	assert num_to_word(42641323862) == 'forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two'
# 	print("All OK BROTHER")

if __name__ == '__main__':
	main()
	
