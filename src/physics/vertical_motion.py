def lastspeed():#ความเร็วปลาย
    gra =  9.80665
    fspeed = int(input("early speed m/s"))
    tim = int(input("time m/s^2"))
    print("Your late speed is %.2f m/s"%(fspeed + (gra * tim)))

def displacement():#การกระจัด
    gra =  9.80665
    fspeed = int(input("early speed m/s"))
    tim = int(input("time m/s^2"))
    print("Your displacement is %.2f m/s"%((fspeed * tim) + (0.5*gra*tim**2)))
