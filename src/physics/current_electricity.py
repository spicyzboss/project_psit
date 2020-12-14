""" Current Electricity """
print("Electric Current")
print("Formula is I = Q/t or Q = It")
def electric_i():
    """ find I """
    print("I = Electric Current (A)")
    print("Q = Amount of electric charge passes through a cross section area (C)")
    print("t = Time when an electric charge passes through a cross section area (s)")
    print("Find I")
    q = float(input("Q : "))
    t = float(input("t : "))
    print("I = %.2f" %(q/t))


def electric_q():
    """ find Q """
    print("Find Q")
    i = float(input("I : "))
    t = float(input("t : "))
    print("Q = %.2f C" %(i*t))


print("Finding electric charge in case of known cross section area")
def electric_know_tuanum_find_i():
    """ Find I """
    print("e = 1.6*(10**(-19))")
    print("v = Electron Speed (m/s)")
    print("A = Cross section area (m^2)")
    print("n = Number of electrons in 1 unit volume (particle/m^3)")
    print("Find I")
    e = 1.6*(10**(-19))
    v = float(input("v : "))
    a = float(input("A : "))
    n = float(input("n : "))
    print("I = %.2f A" %(e*v*a*n))


def electric_know_tuanum_find_v():
    """ Find v """
    print("Find v")
    e = 1.6*(10**(-19))
    i = float(input("I : "))
    a = float(input("A : "))
    n = float(input("n : "))
    print("v = %.2f m/s" %(i/(n*e*a)))


def electric_know_tuanum_find_a():
    """ Find A """
    print("Find A")
    e = 1.6*(10**(-19))
    i = float(input("I : "))
    v = float(input("v : "))
    n = float(input("n : "))
    print("A = %.2f m^2" %(i/(e*v*n)))


def electric_know_tuanum_find_n():
    """ Find n """
    e = 1.6*(10**(-19))
    i = float(input("I : "))
    v = float(input("v : "))
    a = float(input("A : "))
    print("n = %.2f particle/m^3" %(i/(e*v*a)))
