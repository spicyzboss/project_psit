"""CIRCULAR MOTION FUNCTION"""
from time import sleep as delay
import math
#importแค่ฟังคชัน circular_motion

def linear_velocity():
    """LINEAR VELO FUNCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Linear Velocity topic!")
    delay(0.5)
    print()
    print("Which variable do you have?")
    try:
        print("► f (for frequency)\t\t► t (for time)\t\t► w (for angular verocity)")
        type_linear = input("Answer(f/t/w): ").upper()
        print()
        if type_linear == "F":
            delay(0.25)
            print("This Topic will find Linear Velocity from frequency and radius")
            print()
            f_linear = float(input("Input the frequency(Hz): "))
            print()
            r_linear = float(input("Input the radius(m): "))
            v_linear = (2*math.pi*r_linear)*f_linear
            print()
            print("Your Linear Velocity is %.2f m/s"%v_linear)
        elif type_linear == "T":
            delay(0.25)
            print("This Topic will find Linear Velocity from time and radius")
            print()
            t_linear = float(input("Input the time(s): "))
            print()
            r_linear = float(input("Input the radius(m): "))
            v_linear = (2*math.pi*r_linear)/t_linear
            print()
            print("Your Linear Velocity is %.2f m/s"%v_linear)
        elif type_linear == "W":
            delay(0.25)
            print("This Topic will find Linear Velocity from Angular verocity and radius")
            print()
            w_linear = float(input("Input the angular velocity(rad/s): "))
            print()
            r_linear = float(input("Input the radius(m): "))
            v_linear = w_linear*r_linear
            print()
            print("Your Linear Velocity is %.2f m/s"%v_linear)
    except:
        print("Please input in correct format")

    #________________________________END LINEAR VELOCITY____________________________________________________

def angular_velocity():
    """ANGULAR VELO FUNCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Angular Velocity topic!")
    delay(0.5)
    print()
    print("Which variable do you have?")
    try:
        print("► f (for frequency)\t► t (for time)\t► v (for linear verocity)\t► s (for angular displacement)")
        type_angular = input("Answer(f/t/v/s): ").upper()
        print()
        if type_angular == "F":
            delay(0.25)
            print("This Topic will find Angular Velocity from frequency")
            print()
            f_angular = float(input("Input the frequency(Hz): "))
            print()
            w_angular = 2*math.pi*f_angular
            print()
            print("Your Angular Velocity is %.2f rad/s"%w_angular)
        elif type_angular == "T":
            delay(0.25)
            print("This Topic will find Angular Velocity from time")
            print()
            t_angular = float(input("Input the time(s): "))
            print()
            w_angular = (2*math.pi)/t_angular
            print()
            print("Your Angular Velocity is %.2f rad/s"%w_angular)
        elif type_angular == "V":
            delay(0.25)
            print("This Topic will find Angular Velocity from Linear verocity and radius")
            print()
            v_angular = float(input("Input the Linear velocity(m/s): "))
            print()
            r_angular = float(input("Input the radius(m): "))
            w_angular = v_angular/r_angular
            print()
            print("Your Angular Velocity is %.2f rad/s"%w_angular)
        elif type_angular == "S":
            delay(0.25)
            print("This Topic will find Angular Velocity from angular displacement and time")
            print()
            s_angular = float(input("Input the Angular displacement(rad): "))
            print()
            t_angular = float(input("Input the time(s): "))
            w_angular = s_angular/t_angular
            print()
            print("Your Angular Velocity is %.2f rad/s"%w_angular)
    except:
        print("Please input in correct format")
    #________________________________END ANGULAR VELOCITY____________________________________________________

def acceleration_tocenter():
    """ACCELERATION INTO THE CENTER"""
    delay(0.5)
    print("\n")
    print("Welcome to Acceleration into the center topic!")
    delay(0.5)
    try:
        print()
        delay(0.25)
        print("This Topic will find Acceleration from Linear velocity and radius")
        print()
        v_ac = float(input("Input the Linear velocity(m/s): "))
        print()
        r_ac = float(input("Input the radius(m): "))
        print()
        a_ac = (v_ac**2)/r_ac
        print()
        print("Your ac Acceleration into the center is %.2f m/s^2"%a_ac)
    except:
        print("Please input in correct format")
        
    #________________________________END ACCELERATION INTO THE CENTER____________________________________________________

def centipetal_force():
    """CENTRIPETAL FORCE"""
    delay(0.5)
    print("\n")
    print("Welcome to Centripetal Force topic!")
    delay(0.5)
    print()
    print("Which variable do you have?")
    try:
        print("► a (for accelation into the center)\t► v (for linear velocity)\t► w (for angular verocity)")
        type_centforce = input("Answer(a/v/w): ").upper()
        print()
        if type_centforce == "A":
            delay(0.25)
            print("This Topic will find Centripetal Force from Acceleration and Mass")
            print()
            a_centforce = float(input("Input the acceleration(m/s^2): "))
            print()
            m_centforce = float(input("Input the mass(kg): "))
            n_centforce = m_centforce*a_centforce
            print()
            print("Your Centripetal Force is %.2f N"%n_centforce)
        elif type_centforce == "V":
            delay(0.25)
            print("This Topic will find Centripetal Force from Linear velocity, mass and radius")
            print()
            m_centforce = float(input("Input the mass(kg)): "))
            print()
            r_centforce = float(input("Input the radius(m): "))
            print()
            v_centforce = float(input("Input the Linear velocity(m/s): "))
            print()
            n_centforce = m_centforce*((v_centforce**2)/r_centforce)
            print("Your Centripetal Force is %.2f N"%n_centforce)
        elif type_centforce == "W":
            delay(0.25)
            print("This Topic will find Centripetal Force from Angular verocity, mass and radius")
            print()
            m_centforce = float(input("Input the mass(kg)): "))
            print()
            r_centforce = float(input("Input the radius(m): "))
            print()
            w_centforce = float(input("Input the angular velocity(rad/s): "))
            print()
            n_centforce = m_centforce*(w_centforce**2)*r_centforce
            print()
            print("Your Centripetal Force is %.2f N"%n_centforce)
    except:
        print("Please input in correct format")
    #________________________________END Centripetal Force____________________________________________________

def circular_motion():
    """Main Function"""
    print()
    print("CIRCULAR MOTION")
    print()
    print("► Find Linear Velociy\t\t\t► Find Angualar Velociy\n► Find Acceleration into Center\t\t► Find Centripetal Force")
    
    print()
    print("What topic do you want to find?: ", end="")
    type_input_circular = input().upper()
    if type_input_circular == "FIND LINEAR VELOCITY":
        linear_velocity()
    elif type_input_circular == "FIND ANGULAR VELOCITY":
        angular_velocity()
    elif type_input_circular == "FIND ACCELERATION INTO CENTER":
        acceleration_tocenter()
    elif type_input_circular == "FIND CENTRIPETAL FORCE":
        centipetal_force()

#________________________________END MAIN FUNCTION____________________________________________________
