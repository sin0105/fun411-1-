#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab05_1
# 204111 Sec 003

def main():
	test_palindrome_without()


def palindrome_without(text: str, c: str):
	text = text.lower()                # ทำตัวอักษรเป็นพิมพ์เล็กทั้งหมด
	text = text.replace(' ','')        # ลบช่องว่างออก
	text = text.replace(c,'')          # ลบตัวอักษรที่ต้องการ

	if text == '':                     # หากข้อความเป็นช่องว่าง คืนค่าเท็จ
		return False

	if text == text[::-1]:             # เมื่อข้อความเป็นพารินโดม คืนค่าจริง
		return True

	if text != text[::-1]:             # เมื่อข้อความไม่เป็นพารินโดม คืนค่าเท็จ
		return False


def test_palindrome_without():
	assert palindrome_without('Banana','b') is True
	assert palindrome_without('Swap of paws','f') is True
	assert palindrome_without('T','t') is False
	assert palindrome_without('Banana','t') is False
	assert palindrome_without('Never odd or even','f') is True
	print("All OK")

if __name__ == '__main__':
	main()