gra =  9.80665
def lastspeed():#ความเร็วปลาย
    fspeed = int(input("ค่าความเร็วต้น m/s"))
    tim = int(input("เวลา m/s^2"))
    print(fspeed + (gra * tim))
lastspeed()
def Displacement():#การกระจัด
    fspeed = int(input("ค่าความเร็วต้น m/s"))
    tim = int(input("เวลา m/s^2"))
    print((fspeed * tim) + (0.5*gra*tim**2))
Displacement()