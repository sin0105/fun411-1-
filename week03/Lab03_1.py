#!/usr/bin/env python3
# Chonlanna Saikhampa (Aomsin)
# 670510702
# Lab03_1
# 204111 Sec 003

import math

def main():
    # รับข้อมูลพื้นที่ผิวจาก user
    surface_area = float(input("input surface area: "))

    # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
    radius = find_r_from_surface_area(surface_area)

    # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
    volume = sphere_volume(radius)

    # แสดงปริมาตรทรงกลม แบบทศนิยมสองต่ำแหน่ง
    print(f"volume = {volume:.2f}")



def find_r_from_surface_area(surface_area: float) -> float:
    r = (surface_area/(4*math.pi))**0.5
    return r


def sphere_volume(radius: float) -> float:
    v = ((4/3)*math.pi)*radius**3
    return v


if __name__ == '__main__':
    main()