"""PROJECTILE FUNCTION"""
from time import sleep as delay
import math
#importแค่ฟังคชัน projectile()

def u_vector():
    """U VECTOR"""
    delay(0.5)
    print("Welcome to U VECTOR topic!")
    delay(0.5)
    try:
        print()
        delay(0.25)
        print("This Topic will find Ux and Uy from Velocity and the angle")
        print()
        u_u_vector = float(input("Input the Begin Velocity(์m/s): "))
        print()
        seta_u_vector = float(input("Input the Angle of velocity or theta(degree): "))
        print()
        ux_u_vector = u_u_vector*math.cos(math.radians(seta_u_vector))
        uy_u_vector = u_u_vector*math.sin(math.radians(seta_u_vector))
        print()
        print("Your Ux of this Velocity is %.2fcos(%.2f) = %.2f m/s"%(u_u_vector, seta_u_vector, ux_u_vector))
        print()
        print("Your Uy of this Velocity is %.2fsin(%.2f) = %.2f m/s"%(u_u_vector, seta_u_vector, uy_u_vector))
    except:
        print("Please input in correct format")
    #________________________________END U VECTOR____________________________________________________

def x_axis():
    """FIND x_axis"""
    delay(0.5)
    print("Welcome to X Axis topic!")
    delay(0.5)
    print()
    print("Which variable do you want to find?")
    try:
        print("► Sx (for x axis distance)\t\t► Ux (for begin velocity)\t\t► t (for time)")
        type_x_axis = input("Answer(Sx/Ux/t): ").upper()
        print()
        if type_x_axis == "SX":
            delay(0.25)
            print("This Topic will find Distance from begin velocity and time")
            print()
            ux_x_axis = float(input("Input the X axis begin velocity(m/s): "))
            print()
            t_x_axis = float(input("Input the time(s): "))
            sx_x_axis = ux_x_axis*t_x_axis
            print()
            print("Your X axis distance is %.2f m"%sx_x_axis)
        elif type_x_axis == "UX":
            delay(0.25)
            print("This Topic will find X axis Begin Velocity from distance and time")
            print()
            sx_x_axis = float(input("Input the X axis distance(m): "))
            print()
            t_x_axis = float(input("Input the time(s): "))
            ux_x_axis = sx_x_axis/t_x_axis
            print()
            print("Your X axis Begin Velocity is %.2f m/s"%ux_x_axis)
        elif type_x_axis == "T":
            delay(0.25)
            print("This Topic will find Time from distance and velocity")
            print()
            sx_x_axis = float(input("Input the X axis distance(m): "))
            print()
            ux_x_axis = float(input("Input the X axis Begin Velocity(m/s): "))
            t_x_axis = sx_x_axis/ux_x_axis
            print()
            print("Your X axis Begin Velocity is %.2f s"%t_x_axis)
    except:
        print("Please input in correct format")
    #________________________________END X AXIS____________________________________________________

def y_axis():
    """FIND Y AXIS"""
    delay(0.5)
    print("Welcome to Y Axis topic!")
    delay(0.5)
    print()
    print("Which variable do you want to find?")
    try:
        print("► Sy (for y axis distance)\t\t► t (for time)\n► Uy (for begin velocity)\t\t► Vy (for last velocity)")
        type_y_axis = input("Answer(Sy/Uy/Vy/t): ").upper()
        print()
        if type_y_axis == "SY":
            delay(0.25)
            print("Which variable do you have?")
            print("► v&u&t (for Vy Uy and time)")
            print("► g&u&t (for Gravity Accelaeration Uy and time)")
            print("► v&u&g (for Vy Uy and Gravity Acceleration)")
            print()
            type_sy = input("Answer(v&u&t/g&u&t/v&u&g): ").upper()
            print()
            if type_sy == "V&U&T":
                print("This Topic will find Distance from last velocity, begin velocity and time")
                print()
                vy_sy = float(input("Input the Y axis last velocity(m/s): "))
                print()
                uy_sy = float(input("Input the Y axis begin velocity(m/s): "))
                print()
                t_sy = float(input("Input the time(s): "))
                sy_sy = ((vy_sy+uy_sy)/2)*t_sy
                print()
                print("Your Y axis distance is %.2f m"%sy_sy)

            elif type_sy == "G&U&T":
                print("This Topic will find Distance from Gravity Acceleration(9.8m/s^2), begin velocity and time")
                print()
                uy_sy = float(input("Input the Y axis begin velocity(m/s): "))
                print()
                t_sy = float(input("Input the time(s): "))
                sy_sy = (uy_sy*t_sy)+((1/2)*9.8*(t_sy**2))
                print()
                print("Your Y axis distance is %.2f m"%sy_sy)

            elif type_sy == "V&U&G":
                print("This Topic will find Distance from Gravity Acceleration(9.8m/s^2), begin velocity and last velocity")
                print()
                vy_sy = float(input("Input the Y axis last velocity(m/s): "))
                print()
                uy_sy = float(input("Input the Y axis begin velocity(m/s): "))
                print()
                sy_sy = (vy_sy**2-uy_sy**2)/(2*9.8)
                print("Your Y axis distance is %.2f m"%sy_sy)

        elif type_y_axis == "T":
            delay(0.25)
            print("Which variable do you have?")
            print("► v&u&g (for Vy Uy and Gravity Acceleration)")
            print("► v&u&s (for Vy Uy and Gravity Y axis distance)")
            print()
            type_t = input("Answer(v&u&g/v&u&s): ").upper()
            print()
            if type_t == "V&U&G":
                print("This Topic will find Time from last velocity, begin velocity and Gravity Acceleration(9.8m/s^2)")
                print()
                vy_t = float(input("Input the Y axis last velocity(m/s): "))
                print()
                uy_t = float(input("Input the Y axis begin velocity(m/s): "))
                t_t = (vy_t-uy_t)/9.8
                print()
                print("Your Time is %.2f s"%t_t)

            elif type_t == "V&U&S":
                print("This Topic will find Time from Y axis distance, begin velocity and last velocity")
                print()
                vy_t = float(input("Input the Y axis last velocity(m/s): "))
                print()
                uy_t = float(input("Input the Y axis begin velocity(m/s): "))
                print()
                sy_t = float(input("Input the Y axis distance(m): "))
                print()
                t_t = (sy_t*2)/(vy_t+uy_t)
                print("Your Y axis distance is %.2f m"%t_t)

        elif type_y_axis == "UY":
            delay(0.25)
            print("Which variable do you have?")
            print("► v&g&t (for Vy Gravity Accelaeration and time)")
            print("► s&v&t (for Y axis distance Vy and time)")
            print("► s&g&t (for Y axis distance Gravity Acceleration and time)")
            print("► v&g&s (for Vy Gravity Acceleration and Y axis distance)")
            print()
            type_uy = input("Answer(v&g&t/s&v&t/s&g&t/v&g&s): ").upper()
            print()
            if type_uy == "V&G&T":
                print("This Topic will find Begin velocity from last velocity, Gravity Acceleration(9.8 m/s^2) and time")
                print()
                vy_uy = float(input("Input the Y axis last velocity(m/s): "))
                print()
                t_uy = float(input("Input the time(s): "))
                uy_uy = vy_uy-(9.8*t_uy)
                print()
                print("Your Y axis begin velocity is %.2f m/s"%uy_uy)

            elif type_uy == "S&V&T":
                print("This Topic will find Begin velocity  from Y axis distance, last velocity and time")
                print()
                sy_uy = float(input("Input the Y axis distance(m): "))
                print()
                vy_uy = float(input("Input the Y axis last velocity(m/s): "))
                print()
                t_uy = float(input("Input the time(s): "))
                uy_uy = (sy_uy*2/t_uy)-vy_uy
                print()
                print("Your Y axis begin velocity is %.2f m/s"%uy_uy)

            elif type_uy == "S&G&T":
                print("This Topic will find Begin velocity from Y axis distance, Gravity Acceleration(9.8 m/s^2) and time")
                print()
                sy_uy = float(input("Input the Y axis distance(m): "))
                print()
                t_uy = float(input("Input the time(s): "))
                uy_uy = (sy_uy-((1/2)*9.8*(t_uy**2)))/t_uy
                print()
                print("Your Y axis begin velocity is %.2f m/s"%uy_uy)

            elif type_uy == "V&G&S":
                print("This Topic will find Begin velocity from last velocity, Gravity Acceleration(9.8 m/s^2) and Y axis distance")
                print()
                vy_uy = float(input("Input the Y axis last velocity(m/s): "))
                print()
                s_uy = float(input("Input the Y axis distance(m): "))
                uy_uy = math.sqrt((vy_uy**2)-(2*9.8*s_uy))
                print()
                print("Your Y axis begin velocity is %.2f m/s"%uy_uy)

        elif type_y_axis == "VY":
            delay(0.25)
            print("Which variable do you have?")
            print("► u&g&t\t\t► f (for Uy Gravity Accelaeration and time)")
            print("► s&u&t\t\t► f (for Y axis distance Uy and time)")
            print("► s&g&t\t\t► f (for Y axis distance Gravity Acceleration and time)")
            print("► u&g&s\t\t► f (for Uy Gravity Acceleration and Y axis distance)")
            print()
            type_vy = input("Answer(u&g&t/s&u&t/s&g&t/u&g&s): ").upper()
            print()
            if type_vy == "U&G&T":
                print("This Topic will find Last velocity from begin velocity, Gravity Acceleration(9.8 m/s^2) and time")
                print()
                uy_vy = float(input("Input the Y axis begin velocity(m/s): "))
                print()
                t_vy = float(input("Input the time(s): "))
                vy_vy = uy_vy+(9.8*t_vy)
                print()
                print("Your Y axis last velocity is %.2f m/s"%vy_vy)

            elif type_vy == "S&U&T":
                print("This Topic will find Last velocity  from Y axis distance, begin velocity and time")
                print()
                sy_vy = float(input("Input the Y axis distance(m): "))
                print()
                uy_vy = float(input("Input the Y axis begin velocity(m/s): "))
                print()
                t_vy = float(input("Input the time(s): "))
                vy_vy = (sy_vy*2/t_vy)-uy_vy
                print()
                print("Your Y axis last velocity is %.2f m/s"%vy_vy)

            elif type_vy == "S&G&T":
                print("This Topic will find Last velocity from Y axis distance, Gravity Acceleration(9.8 m/s^2) and time")
                print()
                sy_vy = float(input("Input the Y axis distance(m): "))
                print()
                t_vy = float(input("Input the time(s): "))
                vy_vy = (sy_vy+((1/2)*9.8*(t_vy**2)))/t_vy
                print()
                print("Your Y axis last velocity is %.2f m/s"%vy_vy)

            elif type_vy == "U&G&S":
                print("This Topic will find Begin velocity from begin velocity, Gravity Acceleration(9.8 m/s^2) and Y axis distance")
                print()
                uy_vy = float(input("Input the Y axis begin velocity(m/s): "))
                print()
                s_vy = float(input("Input the Y axis distance(m): "))
                vy_vy = math.sqrt((uy_vy**2)+(2*9.8*s_vy))
                print()
                print("Your Y axis begin velocity is %.2f m/s"%vy_vy)
    except:
        print("Please input in correct format")
    #________________________________END Y AXIS____________________________________________________

def max_angle():
    """ANGLE THAT MAKE MAX SY AND MAX SX"""
    delay(0.5)
    print("Welcome to Find Angle that make Sy max and Sx max topic!")
    delay(0.5)
    try:
        print()
        delay(0.25)
        print("This Topic will find Angle(degree) from Sxmax and Symax")
        print()
        sy_max_angle = float(input("Input the Sy max(m): "))
        print()
        sx_max_angle = float(input("Input the Sx max(m): "))
        print()
        angle_max_angle = math.degrees(math.atan(sy_max_angle/sx_max_angle*4))
        print()
        print("Your Angle that make Sy max and Sx max is %.2f degree"%(angle_max_angle))
    except:
        print("Please input in correct format")
    #________________________________END MAX ANGLE____________________________________________________

def sy_max():
    """FIND SY MAX"""
    delay(0.5)
    print("Welcome to Find Sy max topic!")
    delay(0.5)
    try:
        print()
        delay(0.25)
        print("This Topic will find Sy max from begin velocity angle(degree) and Gravity acceleration(9.8 m/s^2)")
        print()
        u_symax = float(input("Input the Begin Velocity(m/s): "))
        print()
        angle_symax = float(input("Input the angle(degree): "))
        print()
        symax_symax = ((u_symax**2)*((math.sin(math.radians(angle_symax)))**2))/(2*9.8)
        print()
        print("Your Sy max is %.2f m"%(symax_symax))
    except:
        print("Please input in correct format")
    #________________________________END SY MAX____________________________________________________

def sx_max():
    """FIND SY MAX"""
    delay(0.5)
    print("Welcome to Find Sx max topic!")
    delay(0.5)
    try:
        print()
        delay(0.25)
        print("This Topic will find Sx max from begin velocity angle(degree) and Gravity acceleration(9.8 m/s^2)")
        print()
        u_sxmax = float(input("Input the Begin Velocity(m/s): "))
        print()
        angle_sxmax = float(input("Input the angle(degree): "))
        print()
        sxmax_sxmax = ((u_sxmax**2)*(math.sin(math.radians(angle_sxmax*2))))/9.8
        print()
        print("Your Sx max is %.2f m"%(sxmax_sxmax))
    except:
        print("Please input in correct format")
    #________________________________END SX MAX____________________________________________________

def time_total():
    """FIND TOTAL TIME THAT OBJECT FALL DOWN"""
    delay(0.5)
    print("Welcome to Find total time topic!")
    delay(0.5)
    try:
        print()
        delay(0.25)
        print("This Topic will Total time from begin velocity angle(degree) and Gravity acceleration(9.8 m/s^2)")
        print()
        u_total_time = float(input("Input the Begin Velocity(m/s): "))
        print()
        angle_total_time = float(input("Input the angle(degree): "))
        print()
        total_time_total_time = (2*u_total_time*math.sin(math.radians(angle_total_time)))/9.8
        print()
        print("Your Total time is %.2f s"%(total_time_total_time))
    except:
        print("Please input in correct format")
    #________________________________END TOTAL TIME____________________________________________________

def projectile():
    """Main Function"""
    print()
    print("PROJECTILE MOTION")
    print()
    print("► U Vector\t\t► X axis\t\t► Y axis\n► Find Angle that make Sy/Sx max\n► Find Sy max\t\t► Find Sx max\t\t► Find total time")
    
    print()
    print("What topic do you want to find?: ", end="")
    type_input_projectile = input().upper()
    if type_input_projectile == "U VECTOR":
        u_vector()
    elif type_input_projectile == "X AXIS":
        x_axis()
    elif type_input_projectile == "Y AXIS":
        y_axis()
    elif type_input_projectile == "FIND ANGLE THAT MAKE SY/SX MAX":
        max_angle()
    elif type_input_projectile == "FIND SY MAX":
        sy_max()
    elif type_input_projectile == "FIND SX MAX":
        sx_max()
    elif type_input_projectile == "FIND TOTAL TIME":
        time_total()
#________________________________END MAIN FUNCTION____________________________________________________