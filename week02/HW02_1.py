#!/usr/bin/env python3
#Chonlanna Saikhampa (Aomsin)
#670510702
#HW02_1
#204111 Sec 003

m1 = float(input("Input m1: ")) 
b1 = float(input("Input b1: ")) 
m2 = float(input("Input m2: ")) 
b2 = float(input("Input b2: ")) 

x = m1-m2
b = b2-b1
x = b/x

y =(m1*x)+b1

print("Lines intersect at (%.2f,%.2f)"%(x,y))