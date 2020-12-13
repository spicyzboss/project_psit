"""WORK & ENERGY FUNCTION"""
from time import sleep as delay
import math
#importแค่ฟังคชัน work_energy()

def work():
    """WORK FUNCTION"""
    delay(0.5)
    print("Welcome to Find Work topic!")
    delay(0.5)
    try:
        print()
        delay(0.25)
        print("This Topic will find Work from force and distance")
        print()
        f_work = float(input("Input the Force that acting on the object(์N): "))
        print()
        s_work = float(input("Input the Distance that object move(m): "))
        print()
        seta_work = float(input("Input the Angle of force(degree): "))
        print()
        w_work = f_work*s_work*(math.cos(math.radians(seta_work)))
        print()
        print("Your Work of the object is %.2f J"%w_work)
    except:
        print("Please input in correct format")

    #________________________________END FIND WORK____________________________________________________

def energy():
    """ENERGY FUNCTION"""
    delay(0.5)
    print("Welcome to Find Energy topic!")
    delay(0.5)
    print()
    print("Which Energy do you want to find?")
    try:
        print("► Ep(for Potential Energy)\t► Eep(Elastic Potential Energy)\t► Ek (for Kinetic Energy)")
        type_energy = input("Answer(Ep/Eep/Ek): ").upper()
        print()
        if type_energy == "EP":
            delay(0.25)
            print("This Topic will find Potential Energy from mass, gravity acceleration(9.8 m/s^2) and height of the object")
            print()
            m_energy = float(input("Input the mass(kg): "))
            print()
            h_energy = float(input("Input the height of the object(m): "))
            ep_energy = m_energy*9.8*h_energy
            print()
            print("Your Potential Energy is %.2f J"%ep_energy)
        elif type_energy == "EEP":
            delay(0.25)
            print("This Topic will find Elastic Potential Energy from time and radius")
            print()
            print("Which variable do you have?")
            print("► k (for spring constant value)\t\t► f (for force action on spring)")
            type_eep = input("Answer(k/f): ").upper()
            print()
            if type_eep == "K":
                k_energy = float(input("Input the spring constant vaule(N/m): "))
                print()
                x_energy = float(input("Input the spring retraction(m): "))
                eep_energy = (1/2)*(k_energy)*(x_energy**2)
                print()
                print("Your Elastic Potential Energy is %.2f J"%eep_energy)
            elif type_eep == "F":
                f_energy = float(input("Input the force that acting on spring(N): "))
                print()
                x_energy = float(input("Input the spring retraction(m): "))
                eep_energy = (1/2)*f_energy*x_energy
                print()
                print("Your Elastic Potential Energy is %.2f J"%eep_energy)
        elif type_energy == "EK":
            delay(0.25)
            print("This Topic will find Kinetic Energy from mass and velocity")
            print()
            m_energy = float(input("Input the mass(kg): "))
            print()
            v_energy = float(input("Input the velocity(m/s): "))
            ek_energy = (1/2)*m_energy*(v_energy**2)
            print()
            print("Your Kinetic Energy is %.2f m/s"%ek_energy)
    except:
        print("Please input in correct format")

    #________________________________END FIND ENERGY____________________________________________________

def power():
    """FIND POWER"""
    delay(0.5)
    print("Welcome to Find Power topic!")
    delay(0.5)
    print()
    print("Which variable do you have?")
    try:
        print("► w&t (for work&time)\t\t► f&v (for force&velocity)")
        type_power = input("Answer(w&t/f&v): ").upper()
        print()
        if type_power == "W&T":
            delay(0.25)
            print("This Topic will find Power from work and time")
            print()
            w_power = float(input("Input the Work(J): "))
            print()
            t_power = float(input("Input the time(s): "))
            p_power = w_power/t_power
            print()
            print("Your Power is %.2f W"%p_power)
        elif type_power == "F&V":
            delay(0.25)
            print("This Topic will find Power from force and velocity")
            print()
            f_power = float(input("Input the Force(N): "))
            print()
            v_power = float(input("Input the Velocity(m/s): "))
            p_power = w_power/t_power
            print()
            print("Your Power is %.2f W"%p_power)
    except:
        print("Please input in correct format")

    #________________________________END POWER____________________________________________________

def work_energy():
    """Main Function"""
    print()
    print("WORK & ENERGY")
    print()
    print("► Find Work\t\t► Find Energy\t\t► Find Power")
    print()
    print("What topic do you want to find?: ", end="")
    type_input_circular = input().upper()
    if type_input_circular == "FIND WORK":
        work()
    elif type_input_circular == "FIND ENERGY":
        energy()
    elif type_input_circular == "FIND POWER":
        power()
#________________________________END MAIN FUNCTION____________________________________________________
