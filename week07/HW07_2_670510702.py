#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# HW07_2
# 204111 Sec 003

def main():
	test_medal_allocation()


def medal_allocation(list_a: list[int]):
	sort = sorted(list_a,reverse=True)             # เรียงเลข มาก -> น้อย
	sort = list(filter(lambda x: x != 0,sort))     # ไม่เลือก 0 มาคิดเลย

	gold = list(filter(lambda x: x == max(sort),sort))          # ดึงตัวเยอะสุดออกมา
	back_g = sort[len(gold):]									# ทุกตัวยกเว้นตัวมากสุด
	 
	silver = list(filter(lambda x: x == max(back_g),back_g))    # ดึงตัวเยอะสุดออกมาจากขี้ซากข้อเก่า
	back_s = back_g[len(silver):]														
	 
	bronze = list(filter(lambda x: x == max(back_s),back_s))	# ดึงตัวเยอะสุดออกมาจากขี้ซากข้อเก่า
	 
	result =(gold,silver,bronze)

	if len(gold) == 2:					# gold = 2 silver ต้องว่าง
		result = (gold,[],silver) 
	elif len(gold) >= 3:				# gold >= 3 ช่องอื่นจะไม่ว่าง	
		result = (gold,[],[])
	elif len(silver) >= 2:				# silver >= 2 ช่องสุดท้ายว่าง
		result = (gold,silver,[])
	return result


def test_medal_allocation():
	assert medal_allocation([9, 8, 7, 6, 5, 4, 3, 2]) ==  ([9], [8], [7])
	assert medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]) ==  ([9], [8], [7, 7])
	assert medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]) ==  ([9, 9], [], [8])
	assert medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) ==  ([9, 9, 9, 9], [], [])
	assert medal_allocation([7, 7, 0]) == ([7,7],[],[])
	assert medal_allocation([2,0,1]) == ([2],[1],[])
	assert medal_allocation([0,0,0,0]) == ([],[],[])

	print("All OK BROTHER")

if __name__ == '__main__':
	main()