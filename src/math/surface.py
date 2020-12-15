def triangle():
    typ = input("common, equilateral, right, isosceles >>> ")
    if typ == "common":
        base = int(input("base(cm) >>> "))
        high = int(input("height(cm) >>> "))
        print("Your area is %.2f"%(0.5 * base * high))
    elif typ == "equilateral":
        side = int(input("side(cm) >>> "))
        print("Your area is %.2f"%((3**0.5/4) * (side**2)))
    elif typ == "right":
        sidea = int(input("right angle 1(cm) >>> "))
        sideb = int(input("right angle 2(cm) >>> "))
        anw = sidea * sideb
        print("Your area is %.2f"%(0.5 * anw))
    elif typ == "isosceles":
        base = int(input("base(cm) >>> "))
        sidea = int(input("base side 1(cm) >>> "))
        sideb = int(input("base side 2(cm) >>> "))
        anw = ((sidea * sideb)**2 - (base)**2)**(1/4)
        print("Your area is %.2f" %(base/4 * anw))

def cube():
    typ = input("squre, rectangle, rhombus, parallelogram, kite, trapezoid >>> ")
    if typ == "squre" or typ == "rectangle" or typ == "rhombus" or typ == "parallelogram":
        base = int(input("base(cm) >>> "))
        high = int(input("height(cm) >>> "))
        print("Your area is %.2f"%(base * high))
    elif typ == "kite":
        line1 = int(input("diagonal1(cm) >>> "))
        line2 = int(input("diagonal2(cm) >>> "))
        print("Your area is %.2f"%(line1 * line2 * 0.5))
    elif typ == "trapezoid":
        dif1 = int(input("parallel side 1(cm) >>> "))
        dif2 = int(input("parallel side 2(cm) >>> "))
        high = int(input("height(cm) >>> "))
        print("Your area is %.2f"%(0.5 * high * (dif1+dif2)))

def circle():
    radius = int(input("radius(cm) >>> "))
    print("Your area is %.2f"%(22/7 * radius**2))
