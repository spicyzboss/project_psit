def speed():#อัตราเร็ว
    dis = int(input("displacement m"))
    tim = int(input("time m/s^2"))
    print("Your speed is %.2f m/s"%(dis/tim))

def acceleration():#ความเร่ง
    fspeed = int(input("early speed m/s"))
    lspeed = int(input("่late speed m/s"))
    tim = int(input("time m/s^2"))
    print("Your acceleration is %.2f m/s^2"%(lspeed - fspeed / tim))

def distance():#ระยะทาง
    speed = int(input("speed m/s"))
    tim = int(input("time m/s^2"))
    print("Your distance is %.2f m"%(speed * tim))

def displacement():#การกระจัด
    fspeed = int(input("early speed m/s"))
    lspeed = int(input("่late speed m/s"))
    tim = int(input("time m/s^2"))
    print("Your displacement is %.2f m"%((fspeed + lspeed) * tim/2))

def latespeed():#ความเร็วปลาย
    fspeed = int(input("early speed m/s"))
    acc = int(input("acceleration m/s^2"))
    tim = int(input("time m/s^2"))
    print("Your late speed is %.2f m/s"%(fspeed + (acc * tim)))
