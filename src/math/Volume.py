import math
def Cylinder():#ทรงกระบอก
    radius = int(input("ใส่ค่ารัศมี(cm)"))
    space = math.pi * radius**2
    high = int(input("ใส่ค่าความสูง(cm)"))
    print("%.3f" %(high * space))    
Cylinder()
def cube():#เหลียม
    side = int(input("ใส่ค่าของด้าน(cm)"))
    high = int(input("ใส่ค่าความสูง(cm)"))
    print(side**2 * high, "เหลี่ยม")
cube()
def circle():#วงกลม
    radius = int(input("ใส่ค่ารัศมี(cm)"))
    print(4 * math.pi * radius**3 / 3)
circle()
def pyramid():#ปิรามิด
    typ = input("type(triangle, cube")
    lon = int(input("ใส่ค่าของด้าน(cm)"))
    highl = int(input("ใส่ค่าของด้าน(cm)"))
    high = int(input("ใส่ค่าความสูง(cm)"))
    volume = lon * highl
    if typ == "triangle":
        print((volume * 0.5) * high/3)
    elif typ == "cube":
        print(volume * high/3)
pyramid()
def Conical():#ทรงกรวย
    radius = int(input("ใส่ค่ารัศมี(cm)"))
    high = int(input("ใส่ค่าความสูง(cm)"))
    print(math.pi * radius**2 * high / 3)
Conical()
def prism():#ปริซึม
    typ = input("type(triangle, cube")
    if typ == "triangle" or typ == "cube":
        lon = int(input("ใส่ค่าของด้าน(cm)"))
        highl = int(input("ใส่ค่าของด้าน(cm)"))
        high = int(input("ใส่ค่าความสูง(cm)"))
        volume = lon * highl
        if typ == "triangle":
            print((volume * 0.5) * high)
        elif typ == "cube":
            print(volume * high)
    elif typ == "circle":
        radius = int(input("ใส่ค่ารัศมี(cm)"))
        high = int(input("ใส่ค่าความสูง(cm)"))
        cir = radius * math.pi
        print(cir * high)
prism()
