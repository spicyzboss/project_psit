def speed():#อัตราเร็ว
    dis = int(input())
    tim = int(input())
    print(dis/tim)
speed()
def acceleration():#ความเร่ง
    fspeed = int(input())
    lspeed = int(input())
    tim = int(input())
    print(lspeed - fspeed / tim)
acceleration()
def distance():#ระยะทาง
    speed = int(input())
    tim = int(input())
    print(speed * tim)
distance()
def Displacement():#การกระจัด
    fspeed = int(input())
    lspeed = int(input())
    tim = int(input())
    print((fspeed + lspeed) * tim/2)
Displacement()
def lastspeed():#ความเร็วปลาย
    fspeed = int(input())
    acc = int(input())
    tim = int(input())
    print(fspeed + (acc * tim))
lastspeed()