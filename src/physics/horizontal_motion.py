def speed():#อัตราเร็ว
    dis = int(input("displacement m"))
    tim = int(input("time m/s^2"))
    print(dis/tim, "m/s")

def acceleration():#ความเร่ง
    fspeed = int(input("early speed m/s"))
    lspeed = int(input("่late speed m/s"))
    tim = int(input("time m/s^2"))
    print(lspeed - fspeed / tim, "m/s^2")

def distance():#ระยะทาง
    speed = int(input("speed m/s"))
    tim = int(input("time m/s^2"))
    print(speed * tim, "m")

def displacement():#การกระจัด
    fspeed = int(input("early speed m/s"))
    lspeed = int(input("่late speed m/s"))
    tim = int(input("time m/s^2"))
    print((fspeed + lspeed) * tim/2, "m")

def latespeed():#ความเร็วปลาย
    fspeed = int(input("early speed m/s"))
    acc = int(input("acceleration m/s^2"))
    tim = int(input("time m/s^2"))
    print(fspeed + (acc * tim), "m/s")
