#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW05_1
# 204111 Sec 003

def main():
	test_substitute_once()


def substitute_once(text: str, old: str, new:str):
	if old not in text:        						# หากตัวที่ต้องการแทนค่าไม่มีอยู่ใน text ให้คืนค่า text เหมือนเดิม 
		return text
	if len(old) == 0:          						# หากไม่มีสมาชิกในตัวที่ต้องการแทนค่า ให้คืนค่า ค่าใหม่เป็นค่าว่าง
		new = ""
	index = text.find(old)     						# หาตำแหน่งของข้อความด้วย str.find
	return text[:index]+new+text[index+len(old):]   # นำคำมาเชื่อมต่อกัน [ตั้งแต่เริ่มต้น:ตำแหน่งold]+ตัวใหม่ที่ต้องการเปลี่ยน+[ตำแหน่งold+ความยาวold:จนจบ]
	

def test_substitute_once():
	assert substitute_once('battle','b','c') == 'cattle'
	assert substitute_once('Bidding','i','u') == 'Budding'
	assert substitute_once("doesn't","n't"," not") == "does not"
	assert substitute_once('I like cat',' ','<3') == 'I<3like cat'
	assert substitute_once("ab","b","bbb") == "abbb"
	assert substitute_once("  ","","=") == "  "
	assert substitute_once("cs","","=") == "cs"
	assert substitute_once('baaaaaab','aaa','c') == 'bcaaab'
	assert substitute_once('baa','c','v') == 'baa'
	print("ALL OK")


if __name__ == '__main__':
	main()
