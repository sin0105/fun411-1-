#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW05_3
# 204111 Sec 003

def main():
	test_is_valid_license()


def is_valid_license(license_str: str):
	if len(license_str) < 3:              # ป้ายทะเบียนไม่ควรต่ำกว่า 3 หลัก
		return False
# หลักที่ 1-2 ต้องเป็นตัวหนังสือ หลังจากนั้นต้องเป็นตัวเลข 4ตัว
	if license_str[0:2].isalpha() and license_str[2:].isdigit() and len(license_str[2:]) <= 4:
		return True		
# หลักที่ 1 ต้องเป็นตัวเลข หลักที่ 2-3 ต้องเป็นตัวหนังสือ หลังจากนั้นต้องเป็นตัวเลข 4ตัว													
	elif license_str[0].isdigit() and license_str[1:3].isalpha() and license_str[3:].isdigit() and len(license_str[3:]) <= 4:
		return True
	else:
		return False

def test_is_valid_license():
	assert is_valid_license('AB89542') is False
	assert is_valid_license('9DL1234') is True
	assert is_valid_license('AB8952') is True
	assert is_valid_license('9999') is False
	assert is_valid_license('CD700') is True
	assert is_valid_license('9DL12394') is False
	assert is_valid_license('99D1234') is False
	assert is_valid_license('991234') is False
	assert is_valid_license('A12') is False
	assert is_valid_license('A') is False
	assert is_valid_license('9') is False
	assert is_valid_license('MM7A') is False
	assert is_valid_license('MMMA') is False
	assert is_valid_license('MM79L') is False

	print("ALL OK")

if __name__ == '__main__':
	main()














