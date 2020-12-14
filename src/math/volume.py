import math

def cylinder():#ทรงกระบอก
    radius = int(input("radius(cm) >>> "))
    space = math.pi * radius**2
    high = int(input("height(cm) >>> "))
    print("%.3f" %(high * space))

def cube():#เหลียม
    side = int(input("side(cm) >>> "))
    high = int(input("height(cm) >>> "))
    print("%.3f" %(side**2 * high))

def circle():#วงกลม
    radius = int(input("radius(cm) >>> "))
    print("%.3f" %(4 * math.pi * radius**3 / 3))

def pyramid():#ปิรามิด
    typ = input("triangle, cube >>> ")
    lon = int(input("side1(cm) >>> "))
    highl = int(input("side2(cm) >>> "))
    high = int(input("height(cm) >>> "))
    volume = lon * highl
    if typ == "triangle":
        print("%.3f" %((volume * 0.5) * high/3))
    elif typ == "cube":
        print("%.3f" %(volume * high/3))

def conical():#ทรงกรวย
    radius = int(input("radius(cm) >>> "))
    high = int(input("height(cm) >>> "))
    print("%.3f" %(math.pi * radius**2 * high / 3))

def prism():#ปริซึม
    typ = input("triangle, cube >>> ")
    if typ == "triangle" or typ == "cube":
        lon = int(input("side1(cm) >>> "))
        highl = int(input("side2(cm) >>> "))
        high = int(input("height(cm) >>> "))
        volume = lon * highl
        if typ == "triangle":
            print("%.3f" %((volume * 0.5) * high))
        elif typ == "cube":
            print(volume * high)
    elif typ == "circle":
        radius = int(input("radius(cm) >>> "))
        high = int(input("height(cm) >>> "))
        cir = radius * math.pi
        print("%.3f" %(cir * high))
