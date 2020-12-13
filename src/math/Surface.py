def triangle():
    typ = input("common, equilateral, right, isosceles >>> ")
    if typ == "common":
        base = int(input("ฐาน(cm) >>> "))
        high = int(input("สูง(cm) >>> "))
        print(0.5 * base * high)
    elif typ == "equilateral":
        side = int(input("ด้าน(cm) >>> "))
        print((3**0.5/4) * (side**2))
    elif typ == "right":
        sidea = int(input("ด้านประกอบมุมฉากa(cm) >>> "))
        sideb = int(input("ด้านประกอบมุมฉากb(cm) >>> "))
        anw = sidea * sideb
        print(0.5 * anw)
    elif typ == "isosceles":
        base = int(input("ฐาน(cm) >>> "))
        sidea = int(input("ด้านประกอบฐานa(cm) >>> "))
        sideb = int(input("ด้านประกอบฐานb(cm) >>> "))
        anw = ((sidea * sideb)**2 - (base)**2)**(1/4)
        print("%.3f" %(base/4 * anw))
triangle()
def cube():
    typ = input("squre, rectangle, rhombus, parallelogram, kite, trapezoid >>> ")
    if typ == "squre" or typ == "rectangle" or typ == "rhombus" or typ == "parallelogram":
        base = int(input("ฐาน(cm) >>> "))
        high = int(input("สูง(cm) >>> "))
        print(base * high)
    elif typ == "kite":
        line1 = int(input("เส้นทะแยงมุม1(cm) >>> "))
        line2 = int(input("เส้นทะแยงมุม2(cm) >>> "))
        print(line1 * line2 * 0.5)
    elif typ == "trapezoid":
        dif1 = int(input("ด้านคู่ขนาน1(cm) >>> "))
        dif2 = int(input("ด้านคู่ขนาน2(cm) >>> "))
        high = int(input("สูง(cm) >>> "))
        print(0.5 * high * (dif1+dif2))
cube()
def circle():
    radius = int(input("รัศมี(cm) >>> "))
    print("%.3f" %(22/7 * radius**2))
circle()
