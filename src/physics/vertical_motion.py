def lastspeed():#ความเร็วปลาย
    gra =  9.80665
    fspeed = int(input("early speed m/s"))
    tim = int(input("time m/s^2"))
    print(fspeed + (gra * tim), "m/s")

def displacement():#การกระจัด
    gra =  9.80665
    fspeed = int(input("early speed m/s"))
    tim = int(input("time m/s^2"))
    print((fspeed * tim) + (0.5*gra*tim**2), "m")
