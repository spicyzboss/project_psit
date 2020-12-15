import math

def cylinder():#ทรงกระบอก
    radius = int(input("radius(cm) >>> "))
    space = math.pi * radius**2
    high = int(input("height(cm) >>> "))
    print("Your volume is %.2f" %(high * space))

def cube():#เหลียม
    side = int(input("side(cm) >>> "))
    high = int(input("height(cm) >>> "))
    print("Your volume is %.2f" %(side**2 * high))

def circle():#วงกลม
    radius = int(input("radius(cm) >>> "))
    print("Your volume is %.2f" %(4 * math.pi * radius**3 / 3))

def pyramid():#ปิรามิด
    typ = input("triangle, cube >>> ")
    lon = int(input("side1(cm) >>> "))
    highl = int(input("side2(cm) >>> "))
    high = int(input("height(cm) >>> "))
    volume = lon * highl
    if typ == "triangle":
        print("Your volume is %.2f" %((volume * 0.5) * high/3))
    elif typ == "cube":
        print("Your volume is %.2f" %(volume * high/3))

def conical():#ทรงกรวย
    radius = int(input("radius(cm) >>> "))
    high = int(input("height(cm) >>> "))
    print("Your volume is %.2f" %(math.pi * radius**2 * high / 3))

def prism():#ปริซึม
    typ = input("triangle, cube >>> ")
    if typ == "triangle" or typ == "cube":
        lon = int(input("side1(cm) >>> "))
        highl = int(input("side2(cm) >>> "))
        high = int(input("height(cm) >>> "))
        volume = lon * highl
        if typ == "triangle":
            print("Your volume is %.2f" %((volume * 0.5) * high))
        elif typ == "cube":
            print("Your volume is %.2f" %(volume * high))
    elif typ == "circle":
        radius = int(input("radius(cm) >>> "))
        high = int(input("height(cm) >>> "))
        cir = radius * math.pi
        print("Your volume is %.2f" %(cir * high))
