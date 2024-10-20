#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab06_2
# 204111 Sec 003
# TA FILM


def main():
	list_a = [1,2,3,4]
	dest_rotate_list(list_a,-5)
	print(list_a)


def dest_rotate_list(list_a: list[int], n:int):
	if abs(n) > len(list_a):                     # ให้ค่า n ไม่ติดลบ เพื่อเทียบความยาวของlist_a 
		n = n%len(list_a)                        # นำค่า n หารปัดเศษด้วยความยาวของlist_a เพื่อทำเป็นรูปแบบการวนซ้ำข้อมูล

	list_a[:] = list_a[-n:]+list_a[:-n]          # ตัวหลัง + ตัวหน้า


if __name__ == '__main__':
	main()
	