#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW06_3
# 204111 Sec 003


def main():
	test_moving_average()


def moving_average(list_x: list[float],win_size: int):
	if win_size > len(list_x):       # ถ้า w มีความยาว > จำนวนข้อมูล ให้คืนค่า []
		return []
	rangee = list(range(len(list_x)-(win_size-1)))
	result = list(map(lambda r: (sum(list_x[r:r+(win_size)]))/win_size,rangee))
	return result
	# rengee คือรอบการทำงาน หาจากจำนวนข้อมูล - (w-1) [0:__]
	# result สูตร (sum(list_x[:]))/win_size
	#        เป็นการสไลด์ rengee จบการทำงานที่ rengee + w


def test_moving_average():
	assert moving_average([1,2,3,4,5],2) == [1.5, 2.5, 3.5, 4.5]
	assert moving_average([1,2,3,4,5],3) == [2.0, 3.0, 4.0]
	assert moving_average([1,2,3,4,5],99) == []
	assert moving_average([1,2,3,4,5],1) == [1.0, 2.0, 3.0, 4.0 ,5.0]
	assert moving_average([1,2,3,4,5],5) == [3.0]
	print("ALL OK BROTHER")


if __name__ == '__main__':
	main()
	