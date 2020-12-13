def speed():#อัตราเร็ว
    dis = int(input("การกระจัด m"))
    tim = int(input("เวลา m/s^2"))
    print(dis/tim)
speed()
def acceleration():#ความเร่ง
    fspeed = int(input("ความเร็วต้น m/s"))
    lspeed = int(input("่ความเร็วปลาย m/s"))
    tim = int(input("เวลา m/s^2"))
    print(lspeed - fspeed / tim)
acceleration()
def distance():#ระยะทาง
    speed = int(input("ความเร็ว m/s"))
    tim = int(input("เวลา m/s^2"))
    print(speed * tim)
distance()
def Displacement():#การกระจัด
    fspeed = int(input("ความเร็วต้น m/s"))
    lspeed = int(input("่ความเร็วปลาย m/s"))
    tim = int(input("เวลา m/s^2"))
    print((fspeed + lspeed) * tim/2)
Displacement()
def lastspeed():#ความเร็วปลาย
    fspeed = int(input("ความเร็วต้น m/s"))
    acc = int(input("ความเร่ง m/s^2"))
    tim = int(input("เวลา m/s^2"))
    print(fspeed + (acc * tim))
lastspeed()
