#!/usr/bin/env python3
#Chonlanna Saikhampa (Aomsin)
#670510702
#HW02_2
#204111 Sec 003
x = float(input("x: ")) 
y = float(input("y: ")) 
x = x-1
sumy = (y*(y+1)*(2*y+1))/6
sumx = (x*(x+1)*(2*x+1))/6

ans = sumy-sumx

print("sum is: %.0f"%ans)