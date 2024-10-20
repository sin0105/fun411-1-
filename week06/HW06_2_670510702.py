#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW06_2
# 204111 Sec 003
# TA FILM

def main():

	print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 -9 .
'''))
	print(decode("ilovecat", '''
0 .
1 2 3 4 .
5 6 -1 .
'''))
	print(decode("TilAke", '''
1 .
2 1 -2 -1 .
0 -3 -101 .
'''))


def decode_helper(code_table, str_index):  # รับรหัส 1 ตัว แล้วคืน 1 อักขระที่ถูกต้อง
	
	if str_index == '.':                                  # เจอ . ให้ขึ้นบรรทัดใหม่
		return '\n'
	elif int(str_index) == -len(code_table):              # ถ้า index(ทางลบ<-) = -(จำนวนของข้อมูล)
		return (code_table[int(str_index)])
	elif abs(int(str_index)) > len(code_table)-1:         # index > จำนวนข้อมูล-1(เนื่องจากในข้อมูลเริ่มจาก 0) คืนค่า _
			return '_'	
	else: 
		return (code_table[int(str_index)])               # คืนค่า ข้อมูลที่ตำแหน่ง index นั้น


def decode(code_table, text):
    # แยกรหัสทั้งหมด ให้กลายเป็น list เช่น ['3', '.', '5', '3', '4', '2', '.', ...]
    l_text = text.split()

    # เรียกใช้ฟังก์ชัน decode_helper() ที่มีหน้าที่รับรหัสหนึ่งตัว แล้วคืน 1 อักขระที่ถูกต้อง
    result_list = list(map(lambda x: decode_helper(code_table, x), l_text))

    # รวม list ของอักขระ ให้เป็น string
    result = ''.join(result_list)
    return result


if __name__ == '__main__':
    main()

