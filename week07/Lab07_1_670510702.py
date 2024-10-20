#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab07_1
# 204111 Sec 003
# TA FILM

def main():
	n = 10
	print(corner_frame(n))


def corner_frame(n: int):
	rangee = list(range(1,n+1))   # รอบการทำ

	text = list(rangee)           # text -> [1,2,..,n]

	new = list(map(lambda r: [r+1]*r+text[r:],rangee))        # เริ่มคิดที่ r+1 เพราะไม่คิดแถวแรก [2]*2 เพิ่มจำนวนตามแถว + ตัวหลังที่เหลือ
	new.pop()												  # เอาตัวสุดท้ายออก เพราะ new ตัวแรกคืนค่าสุดท้ายเป็น [] ซึ่งเราไมต้องการจึงเอาออก

	l_strip = list(map(lambda n: str(n).strip('[]'),new))     # เอา [] ออก

	result = str(text).strip('[]').replace(',','')+'\n'+'\n'.join(l_strip).replace(',','')+'\n'     # หัว  (+)  ตัว 
	return result                                             	


if __name__ == '__main__':
	main()