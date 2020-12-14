""" Resistor """
print("Resistor")
def electrical_resistivity_r():
    """ Electrical Resistivity """
    print("Electrical Resistivity")
    print("Formula is R = p(I/A)")
    print("R = Object resistance (Ω)")
    print("p = Electrical resistivity of the object (Ω*m)")
    print("I = Object length (m)")
    print("A = Cross-sectional area of ​​the object (m^2)")
    print("Find R")
    p = float(input("p : "))
    i = float(input("I : "))
    a = float(input("A : "))
    print("R = %.2f Ω\n" %(p*(i/a)))


def electrical_resistivity_p():
    """ Find p """
    print("Electrical Resistivity")
    print("Formula is R = p(I/A)")
    print("R = Object resistance (Ω)")
    print("p = Electrical resistivity of the object (Ω*m)")
    print("I = Object length (m)")
    print("A = Cross-sectional area of ​​the object (m^2)")
    print("Find p")
    r = float(input("R : "))
    i = float(input("I : "))
    a = float(input("A : "))
    print("p = %.2f Ω*m\n" %((r*a)/i))


def electrical_resistivity_i():
    """ Find p """
    print("Electrical Resistivity")
    print("Formula is R = p(I/A)")
    print("R = Object resistance (Ω)")
    print("p = Electrical resistivity of the object (Ω*m)")
    print("I = Object length (m)")
    print("A = Cross-sectional area of ​​the object (m^2)")
    print("Find I")
    p = float(input("p : "))
    r = float(input("R : "))
    a = float(input("A : "))
    print("I = %.2f m\n" %((r*a)/p))

def electrical_resistivity_a():
    """ Find A """
    print("Electrical Resistivity")
    print("Formula is R = p(I/A)")
    print("R = Object resistance (Ω)")
    print("p = Electrical resistivity of the object (Ω*m)")
    print("I = Object length (m)")
    print("A = Cross-sectional area of ​​the object (m^2)")
    print("Find A")
    p = float(input("p : "))
    r = float(input("R : "))
    i = float(input("I : "))
    print("A = %.2f m^2\n" %((p*i)/r))


def electrical_conductivity_p():
    """ Electrical_Conductivity """
    print("Electrical Conductivity")
    print("Formula is p = 1/σ")
    print("p = Electrical Resistivity of the object (Ω*m)")
    print("σ = Electrical Conductivity of the object (Ω*m)^-1\n")
    print("Find p")
    q = float(input("σ : "))
    print("p = %.2f Ω*m\n" %(1/q))


def electrical_conductivity_q():
    """ Find q """
    print("Electrical Conductivity")
    print("Formula is p = 1/σ")
    print("p = Electrical Resistivity of the object (Ω*m)")
    print("σ = Electrical Conductivity of the object (Ω*m)^-1\n")
    print("Find q")
    p = float(input("p : "))
    print("σ = %.2f (Ω*m)^-1\n" %(1/p))

