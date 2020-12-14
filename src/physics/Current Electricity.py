""" Current Electricity """
""" เดี๋ยวแก้เป็น Eng """
print("Electric Current")
print("Formula is I = Q/t หรือ Q = It")
def electric_i():
    """ find I """
    print("I = Electric Current (A)")
    print("Q คือ ปริมาณประจุไฟฟ้าที่ผ่านภาคตัด (C)")
    print("t คือ เวลาที่ประจุไฟฟ้าเคลื่อนที่ผ่านภาคตัด (s)")
    print("Find I")
    q = float(input("Q : "))
    t = float(input("t : "))
    print("I = %.2f" %(q/t))
electric_i()

def electric_q():
    """ find Q """
    print("Find Q")
    i = float(input("I : "))
    t = float(input("t : "))
    print("Q = %.2f C" %(i*t))
electric_q()

print("การหากระแสไฟฟ้าในกรณีที่ทราบพื้นที่หน้าตัดของตัวนำ")
def electric_know_tuanum_find_i():
    """ Find I """
    print("e = 1.6*(10**(-19))")
    print("v คือ ความเร็วรอยเลื่อนของอิเล็กตรอน (m/s)")
    print("A คือ พื้นที่หน้าตัดของตัวนำ (m^2)")
    print("n คือ จำนวนอิเล็กตรอนใน 1 หน่วยปริมาตร (อนุภาค/m^3)")
    print("Find I")
    e = 1.6*(10**(-19))
    v = float(input("v : "))
    a = float(input("A : "))
    n = float(input("n : "))
    print("I = %.2f A" %(e*v*a*n))
electric_know_tuanum_find_i()

def electric_know_tuanum_find_v():
    """ Find v """
    print("Find v")
    e = 1.6*(10**(-19))
    i = float(input("I : "))
    a = float(input("A : "))
    n = float(input("n : "))
    print("v = %.2f m/s" %(i/(n*e*a)))
electric_know_tuanum_find_v()

def electric_know_tuanum_find_a():
    """ Find A """
    print("Find A")
    e = 1.6*(10**(-19))
    i = float(input("I : "))
    v = float(input("v : "))
    n = float(input("n : "))
    print("A = %.2f m^2" %(i/(e*v*n)))
electric_know_tuanum_find_a()

def electric_know_tuanum_find_n():
    """ Find n """
    e = 1.6*(10**(-19))
    i = float(input("I : "))
    v = float(input("v : "))
    a = float(input("A : "))
    print("n = %.2f particle/m^3" %(i/(e*v*a)))
electric_know_tuanum_find_n()
