#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW05_2
# 204111 Sec 003

def main():
	test_roman_numeral()


def roman_numeral(n: int):
	return find_thousand(n)+find_hundred(n)+find_ten(n)+find_digit(n)


def find_thousand(n):
	thousand = n//1000                  # หาหลักพัน
	if thousand == 0: return ""         # if 0 คืนค่าว่าง
	if thousand == 1: return "M"		# if 1-4 คืนค่าเลขโรมัน
	if thousand == 2: return "MM"
	if thousand == 3: return "MMM"
	if thousand == 4: return "MMMM"
	

def find_hundred(n):
	hundred = (n%1000)//100				# หลักร้อย
	if hundred == 0: return ""			# if 0 คืนค่าว่าง
	if hundred == 1: return "C"			# if 1-9 คืนค่าเลขโรมัน
	if hundred == 2: return "CC"
	if hundred == 3: return "CCC"
	if hundred == 4: return "CD"
	if hundred == 5: return "D"
	if hundred == 6: return "DC"
	if hundred == 7: return "DCC"
	if hundred == 8: return "DCCC"
	if hundred == 9: return "CM"


def find_ten(n):
	ten = ((n%1000)%100)//10   			# หาหลักสิบ
	if ten == 0: return ""				# if 0 คืนค่าว่าง
	if ten == 1: return "X"				# if 1-9 คืนค่าเลขโรมัน
	if ten == 2: return "XX"
	if ten == 3: return "XXX"
	if ten == 4: return "XL"
	if ten == 5: return "L"
	if ten == 6: return "LX"
	if ten == 7: return "LXX"
	if ten == 8: return "LXXX"
	if ten == 9: return "XC"


def find_digit(n):
	digit = ((n%1000)%100)%10  			# หาหลักหน่วย
	if digit == 0: return ""			# if 0 คืนค่าว่าง
	if digit == 1: return 'I'			# if 1-9 คืนค่าเลขโรมัน
	if digit == 2: return 'II'
	if digit == 3: return 'III'
	if digit == 4: return 'IV'
	if digit == 5: return 'V'
	if digit == 6: return 'VI'
	if digit == 7: return 'VII'
	if digit == 8: return 'VIII'
	if digit == 9: return 'IX'


def test_roman_numeral():
	assert roman_numeral(4) == "IV"
	assert roman_numeral(9) == "IX"
	assert roman_numeral(25) == "XXV"
	assert roman_numeral(267) == "CCLXVII"
	assert roman_numeral(4999) == "MMMMCMXCIX"
	assert roman_numeral(555) == "DLV"
	print("ALL OK")

if __name__ == '__main__':
	main()




'''
def roman(num):
	match num:
		case 0: return ''
		case 1: return 'I'
		case 2: return 'II'
		case 3: return 'III'
		case 4: return 'IV'
		case 5: return 'V'
		case 6: return 'VI'
		case 7: return 'VII'
		case 8: return 'VIII'
		case 9: return 'IX'


def roman_numeral(n):
	digit = n % 10
	ten = (n % 100) // 10
	hundred = (n % 1000) // 100
	thousand = n // 1000

	result = ('M' * thousand) + \
			 roman(hundred).replace('X', 'M').replace('V', 'D').replace('I', 'C') + \
			 roman(ten).replace('X', 'C').replace('V', 'L').replace('I', 'X') + \
			 roman(digit) 
	return result


if __name__ == "__main__":
	print(roman_numeral(1000))
'''
