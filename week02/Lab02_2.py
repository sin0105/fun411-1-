#!/usr/bin/env python3
#Chonlanna Saikhampa (Aomsin)
#670510702
#Lab2_2
#204111 Sec 003

number = int(input("Input milliseconds: ")) # รับค่าทางแป้นพิมพ์
day = number//86400000 # การหารไม่เอาเศษ ต้องการแค่จำนวนวัน
day1 = number%86400000 # หารเอาเศษไปคำนวนหาชั่วโมง
hr = (day1//3600000) # การหารไม่เอาเศษ ต้องการแค่จำนวนชั่วโมง
hr1 = (day1%3600000) # หารเอาเศษไปคำนวนหานาที
minn = (hr1//60000) # การหารไม่เอาเศษ ต้องการแค่จำนวนนาที
minn1 = (hr1%60000) # หารเอาเศษไปคำนวนหาวินาที
sec = (minn1//1000) # การหารไม่เอาเศษ ต้องการแค่จำนวนวินาที
sec1 = (minn1%1000) # หารเอาเศษไปคำนวนหามิลลิวินาที
mill = sec1%1000 # การหารไม่เอาเศษ ต้องการแค่จำนวนมิลลิวินาที

print (day,"day(s)",hr,"hour(s)",minn,"minute(s)",sec,"second(s)",mill,"millisec(s)")