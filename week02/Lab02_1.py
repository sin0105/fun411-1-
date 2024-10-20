#!/usr/bin/env python3
#Chonlanna Saikhampa (Aomsin)
#670510702
#Lab2_1
#204111 Sec 003
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

S = (a+b+c)/2
Area = ((S*(S-a)*(S-b)*(S-c))**(1/2))

print("area:",math.ceil(Area))