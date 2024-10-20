#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab05_2
# 204111 Sec 003

def main():
	test_count_down_to_songkran()

def count_down_to_songkran(d: int, m: int, y: int):
	if m == 1:                               
		day = (31-d)+72
		return day+leap_year(y)
	if m == 2:
		day = (28-d)+44
		return day+leap_year(y)
	if m == 3:
		day = (31-d)+13
		return day
	if m == 4:
		if d <= 13:
			day = (13-d)
			return day
		else:
			day = (30-d)+348
			return day+leap_year(y+1)
	if m == 5:
		day = (31-d)+317
		return day+leap_year(y+1)
	if m == 6:
		day = (30-d)+287
		return day+leap_year(y+1)
	if m == 7:
		day = (31-d)+256
		return day+leap_year(y+1)
	if m == 8:
		day = (31-d)+225
		return day+leap_year(y+1)
	if m == 9:
		day = (30-d)+195
		return day+leap_year(y+1)
	if m == 10:
		day = (31-d)+164
		return day+leap_year(y+1)
	if m == 11:
		day = (30-d)+134
		return day+leap_year(y+1)
	if m == 12:
		day = (31-d)+103
		return day+leap_year(y+1)


def leap_year(y: int):
	if (y % 400 == 0):
		return 1
	elif (y % 100 == 0):
		return 0
	elif (y % 4 == 0):
		return 1
	else:
		return 0


def test_count_down_to_songkran():
	# assert count_down_to_songkran(14,4,99) == 365   # ตามปฏิทินเกเกอเรียน จะไม่คิดปีที่ต่ำกว่า 1580
	assert count_down_to_songkran(14,4,2023) == 365
	assert count_down_to_songkran(1,2,200) == 71
	assert count_down_to_songkran(1,2,1100) == 71
	assert count_down_to_songkran(1,2,2024) == 72
	assert count_down_to_songkran(13,4,2024) == 0
	assert count_down_to_songkran(14,4,2024) == 364
	assert count_down_to_songkran(19,2,2024) == 54
	assert count_down_to_songkran(19,2,2023) == 53
	assert count_down_to_songkran(28,7,2027) == 260
	assert count_down_to_songkran(13,4,2025) == 0
	assert count_down_to_songkran(13,4,2024) == 0
	assert count_down_to_songkran(13,4,2023) == 0
	assert count_down_to_songkran(1,2,2024) == 72 
	assert count_down_to_songkran(4,2,2025) == 68 
	assert count_down_to_songkran(1,1,2024) == 103
	assert count_down_to_songkran(12,4,2024) == 1
	assert count_down_to_songkran(12,4,2025) == 1
	assert count_down_to_songkran(15,2,2024) == 58
	assert count_down_to_songkran(31,3,2024) == 13
	assert count_down_to_songkran(20,3,2024) == 24
	assert count_down_to_songkran(14,4,2024) == 364
	assert count_down_to_songkran(14,4,2025) == 364
	assert count_down_to_songkran(14,4,2023) == 365
	assert count_down_to_songkran(29,2,2024) == 44
	assert count_down_to_songkran(17,5,2024) == 331
	assert count_down_to_songkran(17,6,2024) == 300
	assert count_down_to_songkran(31,12,2024) == 103
	assert count_down_to_songkran(31,12,2025) == 103
	assert count_down_to_songkran(31,12,2023) == 104
	assert count_down_to_songkran(27,10,2023) == 169
	assert count_down_to_songkran(27,10,2024) == 168
	assert count_down_to_songkran(31,10,2024) == 164
	assert count_down_to_songkran(13,10,2024) == 182
	assert count_down_to_songkran(13,10,2023) == 183
	assert count_down_to_songkran(13,10,2023) == 183
	assert count_down_to_songkran(23,8,2023) == 234
	assert count_down_to_songkran(1,4,1600) == 12
	assert count_down_to_songkran(1,4,1600) == 12
	assert count_down_to_songkran(22,7,3000) == 265
	assert count_down_to_songkran(11,11,11) == 154
	print("All OK")

if __name__ == '__main__':
	main()

'''
กำหนดฟังก์ชัน leap year หากเข้าเงื่อนไขให้คืนค่าเป็น 1 หากไม่เข้าเงื่อนไขให้คืนค่าเป็น 0
	เช็คเดือน เพื่อดูว่าจะได้ใช้ leap year กรณีใด
		m = 1,2 	y จะไม่มีทางเดินทางข้ามปี เพราะจะถึงสงกรานต์ก่อนปีถัดไป จึงไม่ต้องคิดกรณีข้ามปีเป็น leap year
		m = 3   	y จะไม่ได้รับผลกระทบใดๆจาก leap year เพราะจะถึงสงกรานต์ก่อนปีถัดไปและไม่เดินทางผ่านเดือนกุมภาพันธุ์
					จึงไม่ต้องคิดกรณีข้ามปีเป็น leap year
		m = 4 		จะแบ่งเป็น 2 กรณี 1)กรณี d <= 13 (ให้นิยามตาม m = 3)
							   	   2)กรณี d > 13 จะเดินทางข้ามปี จึงต้องคิดกรณีข้ามปีเป็น leap year โดยการคิด y+1
		m = 5-12	จะเดินทางข้ามปี จึงต้องคิดกรณีข้ามปีเป็น leap year โดยการคิด y+1

ในแต่ละเดือนจะคืนค่าจำนวนวันไม่เท่ากันจึงเลือกคิดกรณีของทุกเดือน
	เดือนที่ลงท้ายด้วย _คม = 31 วัน    -> m = 1,3,5,7,8,10,12
	เดือนที่ลงท้ายด้วย _พันธ์ = 28      -> m = 2
	เดือนที่ลงท้ายด้วย _ยน = 30 วัน    -> m = 4,6,9
day = (จำนวนวันทั้งหมดของเดือนx - วันที่รับค่าเข้ามา)+จำนวนวันจนถึงวันสงกรานต์(ไม่รวมที่อยู่ในเดือนที่เลือก)
คืนค่า day + 1 (หากเป็น leap year)(y+=1 คิดกรณีที่ข้ามปี)

'''
