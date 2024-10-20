#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW07_1
# 204111 Sec 003

def main():
	test_print_polynomial()


def print_polynomial(pc_list: list[tuple[int,float]], v: str):
	sort = sorted(pc_list,key=lambda x: x[0],reverse=True)  # เรียงตัวเลข มาก -> น้อย
	sort = list(filter(lambda x: x[1] != 0,sort))           # เลือกทุกตัวที่ไม่ใช่ 0 
	if sort == []: return '0'								# เมื่อพบ [] (ซึ่งมาจากการไม่เอา 0)


	# tuple[0] = กำลัง
	# tuple[1] = สปส.
	all_mark = list(map(lambda x:mark(sort[x][1], x),range(0,len(sort)))) 						# ทราบเครื่องหมาย +,- จาก tuple[1],index
	all_coefficient = list(map(lambda x:coefficient(sort[x][1]),range(0,len(sort))))  			# นำค่าใน tuple[1] ไปใส่ในสมการหลัก
	all_variable = list(map(lambda x:str_vari(sort[x][1],sort[x][0],v),range(0,len(sort))))		# นำไปคิด กรณีเป็นค่า (1)(0)
	all_powwer = list(map(lambda x:powwer(sort[x][0]),range(0,len(sort))))						# นำไปคิด กรณีหมวกเจ๊ก ^

	# รวมทุกค่าให้เป็นสมการ 
	result = list(map(lambda m,c,v,p: m+str(c)+v+p, all_mark,all_coefficient,all_variable,all_powwer))
	finall =  ''.join(result)
	return finall


def mark(sort,index):            					# ฟังก์ชัน การเลือกใส่เครื่องหมาย _+_,_-_
	if index == 0:										# 0 -> ค่าว่าง
		if sort > 0:									# (I-) -> (_-_)
			return ''            						# (I+) -> (_+_)
		elif sort == 0:								# เมื่อเป็น [0]
			return ''									# (I-) -> (-)
		else: return '-'								# (I+) -> (+)
	else:
		if sort > 0:
			return ' + '
		else: return ' - '


def coefficient(sort):								# ฟังก์ชัน สปส.
	if sort == 0 :									# สปส.เป็น 0 ไม่คืนค่า
		return ''
	elif abs(sort) > 0 and abs(sort) != 1:			# กรณีที่ สปส.เป็น 0 และ ไม่เป็น 1 คืนค่า sort 
		return abs(sort)
	else: return ''


def str_vari(sort,num,v):							# ฟังก์ชันตัวแปร v
	if abs(sort) == 1 and num == 0:					# เมื่อ สปส. = 1 และ กำลัง = 0 พร้อมกัน คืนค่า 1
		return '1'
	elif abs(sort) == 1 and num == 1:				# เมื่อ สปส. = 1 และ กำลัง = 1 พร้อมกัน คืนค่า v
		return v
	elif num == 0:									# เมื่อกำลังเป็น 0 จะไม่คืนค่าใดๆ
		return ''
	else: return v


def powwer(num):									# ฟังก์ชันยกกำลัง คืนค่าหมวกเจ๊ก ^
	if num == 0:									# กำลังเป็น 0 ไม่คืนค่า
		return ''
	elif num > 1:									# เมื่อกำลัง >1 คืนค่าหมวกเจ๊ก ^ + 'กำลังนั้น'
		return '^'+str(num)
	else: return ''


def test_print_polynomial():
	assert print_polynomial([(1,-6)], 'x') == "-6x"
	assert print_polynomial([(1, 1)], 'x') == "x"
	assert print_polynomial([(2, 0), (1, -1)], 'x') == "-x"
	assert print_polynomial([(1, -1)], 'v') == "-v"
	assert print_polynomial([(2, -1)], "x") == "-x^2"
	assert print_polynomial([(191, 2)], "x") == "2x^191"
	assert print_polynomial([(0, 1)], 'x') == "1"
	assert print_polynomial([(1, 0)], 'y') == "0"
	assert print_polynomial([(0, 0)], 'x') == "0"
	assert print_polynomial([(0, 0), (1, 0)], 'h') == "0"

	assert print_polynomial([(0, -6.5), (1, 0.1)], 'x') == "0.1x - 6.5"
	assert print_polynomial([(0, -6.5), (1, -0.1)], 'x') == "-0.1x - 6.5"
	assert print_polynomial([(0, -4), (1, 0.5)], "x") == "0.5x - 4"
	assert print_polynomial([(1, 0.5), (0, 2.3)], "x") == "0.5x + 2.3"

	assert print_polynomial([(1, -1), (0, -1)], 'x') == "-x - 1"
	assert print_polynomial([(1, 1), (0, -1)], 'y') == "y - 1"
	assert print_polynomial([(3, 0), (0, 1), (1, -1)], 'x') == "-x + 1"
	assert print_polynomial([(2, 34), (0, -1)], "y") == "34y^2 - 1"
	assert print_polynomial([(0, -15), (2, 1), (3, 0)], "x") == "x^2 - 15"
	assert print_polynomial([(3, 2), (0, 8), (1, -1)], "x") == "2x^3 - x + 8"
	assert print_polynomial([(3, -2), (0, 8), (1, 1)], "x") == "-2x^3 + x + 8"
	assert print_polynomial([(19, 1), (10, 2)], "x") == "x^19 + 2x^10"
	assert print_polynomial([(109, 1), (10, 2)], "x") == "x^109 + 2x^10"
	assert print_polynomial([(109, -1), (11, 1)], "x") == "-x^109 + x^11"
	assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'x') == "-6x^2 + 34x - 8"
	assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'y') == "-6y^2 + 34y - 8"
	assert print_polynomial([(2,6), (0,-8), (1,34)], 'x') == "6x^2 + 34x - 8"
	assert print_polynomial([(2,6), (0,-8), (1,34), (5, -21)], 'x') == "-21x^5 + 6x^2 + 34x - 8"
	assert print_polynomial([(100,6), (0,-8), (1,34), (5, -21)], 'x') == "6x^100 - 21x^5 + 34x - 8"

	print("All OK BROTHER")


if __name__ == '__main__':
	main()