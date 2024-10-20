#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW06_1
# 204111 Sec 003


def main():
	test_uniform()


def uniform(line: str):
	len_up = len(list(filter(lambda word: word.isupper(),line)))   # หาจำนวนตัวพิมพ์ใหญ่ทั้งหมดใน line โดยการ filter isupper
	len_low = len(list(filter(lambda word: word.islower(),line)))  # หาจำนวนตัวพิมพ์เล็กทั้งหมดใน line โดยการ filter isupper
	alpha = (list(filter(lambda word: word.isalpha(),line)))[0]    # หาตัวอักษรตัวแรกที่เป็น alphabet

	if len_up > len_low :           # จำนวนตัวพิมพ์ใหญ่ > จำนวนตัวพิมพ์เล็ก ให้คืนค่า ตัวหนังสือทั้งหมดเป็นตัวพิมพ์ใหญ่
		return line.upper()
	elif len_up < len_low:          # จำนวนตัวพิมพ์ใหญ่ < จำนวนตัวพิมพ์เล็ก ให้คืนค่า ตัวหนังสือทั้งหมดเป็นตัวพิมพ์เล็ก
		return line.lower()
	else:                           # จำนวนตัวพิมพ์ใหญ่ = จำนวนตัวพิมพ์เล็ก 
		if alpha.isupper():         # หากตัวอักษรตัวแรกเป็็นตัวพิมพ์ใหญ่ ให้คืนค่า ตัวหนังสือทั้งหมดเป็นตัวพิมพ์ใหญ่
			return line.upper()
		else:                       # หากตัวอักษรตัวแรกเป็็นตัวพิมพ์เล็ก ให้คืนค่า ตัวหนังสือทั้งหมดเป็นตัวพิมพ์เล็ก
			return line.lower()


def test_uniform():
	assert uniform('HaPpY') == 'HAPPY'
	assert uniform('HaPpYyy') == 'happyyy'
	assert uniform('cOdINg') == 'coding'
	assert uniform('coMP scI!!!') == 'comp sci!!!'
	assert uniform('????WhAt') == '????WHAT'
	assert uniform('?wH?at THE cA?t') == '?wh?at the ca?t'
	print("ALL OK BROTHER")


if __name__ == '__main__':
	main()
	