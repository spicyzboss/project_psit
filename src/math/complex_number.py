"""COM PLEX NUMBER FUNCTION"""
from time import sleep as delay
import math
import json
#import แค่ฟังคชันชื่อ complex_number()

def made_sym(num):
    """MADE SYMBOL FOR PRINT"""
    if num >= 0:
        ans = "+"+str("%.2f"%num)
    elif num < 0:
        ans = str("%.2f"%num)
    return ans

def find_i():
    """FIND I^N"""
    delay(0.5)
    print("\n")
    print("Welcome to Find I^N topic!  (\"^\" mean Exponential)")
    delay(0.5)
    print()
    type_i_complex = int(input("Input the Exponent of I: "))
    print()
    i_calculate = type_i_complex%4
    if i_calculate == 1:
        print("Your Answer of I^%d is i"%(type_i_complex))
    elif i_calculate == 2:
        print("Your Answer of I^%d is -1"%(type_i_complex))
    elif i_calculate == 3:
        print("Your Answer of I^%d is -i"%(type_i_complex))
    elif i_calculate == 0:
        print("Your Answer of I^%d is 1"%(type_i_complex))
    
#_____________________________________END I^N______________________________________

def normal_complex_number():
    """NORMAL COMPLEX FUNCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Normal Complex Number topic!")
    delay(0.5)
    print()
    print("Which one do you want to find?")
    print("► Calculate the complex number\t► Find Inverse of complex number\t► Find Conjugate of complex number")
    print("Answer: ", end="")
    type_normal_complex = input().upper()
    print()
    if type_normal_complex == "CALCULATE THE COMPLEX NUMBER":
        delay(0.25)
        print("This Topic will find result of +, - ,* of Normal complex number")
        try:
            print()
            type_cal_normal = input("Input the Symbol of calculate(+ for addition, - for differential and * for multiply): ")
            if type_cal_normal == "+":
                print()
                print("From Z1 = A1+B1i and Z2 = A2+B2i")
                a1_sum_nor = float(input("Input A1: "))
                b1_sum_nor = float(input("Input B1: "))
                print()
                a2_sum_nor = float(input("Input A2: "))
                b2_sum_nor = float(input("Input B2: "))
                print()
                print("Your Answer of Z1+Z2 is %.2f%si"%((a1_sum_nor+a2_sum_nor),made_sym(b1_sum_nor+b2_sum_nor)))
            elif type_cal_normal == "-":
                print()
                print("From Z1 = A1+B1i and Z2 = A2+B2i")
                a1_dif_nor = float(input("Input A1: "))
                b1_dif_nor = float(input("Input B1: "))
                print()
                a2_dif_nor = float(input("Input A2: "))
                b2_dif_nor = float(input("Input B2: "))
                print()
                print("Your Answer of Z1-Z2 is %.2f%si"%((a1_dif_nor-a2_dif_nor),made_sym(b1_dif_nor-b2_dif_nor)))
            elif type_cal_normal == "*":
                print()
                print("From Z1 = A1+B1i and Z2 = A2+B2i")
                a1_mul_nor = float(input("Input A1: "))
                b1_mul_nor = float(input("Input B1: "))
                print()
                a2_mul_nor = float(input("Input A2: "))
                b2_mul_nor = float(input("Input B2: "))
                print()
                print("Your Answer of Z1*Z2 is %.2f%si"%((a1_mul_nor*a2_mul_nor)-(b1_mul_nor*b2_mul_nor),made_sym((a1_mul_nor*b2_mul_nor)+(b1_mul_nor*a2_mul_nor))))
        except:
            print("Please input in correct format")
        
    #________________________________END CALCULATE NORMAL COMPLEX____________________________________________________

    elif type_normal_complex == "FIND INVERSE OF COMPLEX NUMBER":
        delay(0.25)
        print("This Topic will find inverse of complex number")
        try:
            print()
            print("From Z = A+Bi")
            a_inverse = float(input("Input A: "))
            b_inverse = float(input("Input B: "))
            print()
            divide_inverse = (a_inverse**2)+(b_inverse**2)
            a_inverse = a_inverse/divide_inverse
            b_inverse = (b_inverse*-1)/divide_inverse
            print("Your Inverse Complex number is Z = %.2f%si"%(a_inverse,made_sym(b_inverse)))
        except:
            print("Please input in correct format")
        
    #________________________________END INVERSE NORMAL COMPLEX____________________________________________________

    elif type_normal_complex == "FIND CONJUGATE OF COMPLEX NUMBER":
        delay(0.25)
        print("This Topic will find conjugate of complex number")
        try:
            print()
            print("From Z = A+Bi")
            a_conjugate = float(input("Input A: "))
            b_conjugate = float(input("Input B: "))
            print()
            b_conjugate = b_conjugate*-1
            print("Your Conjugate Complex number is Z = %.2f%si"%(a_conjugate,made_sym(b_conjugate)))
        except:
            print("Please input in correct format")
        
    #________________________________END CONJUGATE NORMAL COMPLEX____________________________________________________

#________________________________END NORMAL COMPLEX NUMBER____________________________________________________

def polar_complex_number():
    """POLAR COMPLEX NUMBER"""
    delay(0.5)
    print("\n")
    print("Welcome to Polar Complex Number topic!")
    delay(0.5)
    print()
    print("Which one do you want to find?")
    print("► Find Polar form of complex number\t\t► Calculate the complex number")
    print("Answer: ", end="")
    type_polar_complex = input().upper()
    print()
    if type_polar_complex == "FIND POLAR FORM OF COMPLEX NUMBER":
        delay(0.25)
        print("This Topic will find Polar Form from Normal complex number")
        try:
            print()
            print("From Z = A+Bi")
            a_polar_find = float(input("Input A: "))
            b_polar_find = float(input("Input B: "))
            tan_polar_find = b_polar_find/a_polar_find
            r_polar_find = math.sqrt(a_polar_find**2+b_polar_find**2)
            angle_polar_find = math.degrees(math.atan(tan_polar_find))
            c_polar_find = r_polar_find
            cos_polar_find = a_polar_find/c_polar_find
            sin_polar_find = b_polar_find/c_polar_find
            print()
            print("Your Polar Complex number is Z = %.2f(cos(%.2f)+isin(%.2f))"%(r_polar_find,angle_polar_find,angle_polar_find))
        except:
            print("Please input in correct format")
    elif type_polar_complex == "CALCULATE THE COMPLEX NUMBER":
        delay(0.25)
        print("This Topic will find result of *, / , ^, root of Polar complex number")
        try:
            print()
            type_cal_polar = input("Input the Symbol of calculate(* for multiply, / for divided, ^ for Exponential and root for find N root): ").upper()
            if type_cal_polar == "*":
                print()
                print("From Z1 = R1(cosA + isinA) and Z2 = R2(cosB + isinB)")
                a_mul_pol = float(input("Input A(degree): "))
                b_mul_pol = float(input("Input B(degree): "))
                print()
                r1_mul_pol = float(input("Input R1: "))
                r2_mul_pol = float(input("Input R2: "))
                print()
                print("Your Answer of Z1*Z2 is %.2f(cos(%.2f) + isin(%.2f))"%(r1_mul_pol*r2_mul_pol, a_mul_pol+b_mul_pol, a_mul_pol+b_mul_pol))
            elif type_cal_polar == "/":
                print()
                print("From Z1 = R1(cosA + isinA) and Z2 = R2(cosB + isinB)")
                a_div_pol = float(input("Input A(degree): "))
                b_div_pol = float(input("Input B(degree): "))
                print()
                r1_div_pol = float(input("Input R1: "))
                r2_div_pol = float(input("Input R2: "))
                print()
                print("Your Answer of Z1/Z2 is %.2f(cos(%.2f) + isin(%.2f))"%(r1_div_pol/r2_div_pol, a_div_pol-b_div_pol, a_div_pol-b_div_pol))
            elif type_cal_polar == "^":
                print()
                print("From Z1 = R(cosA + isinA)")
                a_expo_pol = float(input("Input A(degree): "))
                r_expo_pol = float(input("Input R: "))
                print()
                n_expo_pol = float(input("Input Exponent(N): "))
                print()
                print("Your Z^N is %.2f(cos(%.2f) + isin(%.2f))"%(r_expo_pol**n_expo_pol, a_expo_pol*n_expo_pol, a_expo_pol*n_expo_pol))
            elif type_cal_polar == "ROOT":
                print()
                print("From Z1 = R(cosA + isinA)")
                a_root_pol = float(input("Input A(degree): "))
                r_root_pol = float(input("Input R: "))
                print()
                n_root_pol = float(input("Input N root: "))
                print()
                for k in range(int(n_root_pol)):
                    print("Your n√Z is %.2f(cos(%.2f) + isin(%.2f))"%(r_root_pol*(1/n_root_pol), (a_root_pol/n_root_pol)+(k*(360/3)), (a_root_pol/n_root_pol)+(k*(360/3))))
        except:
            print("Please input in correct format")
        
    #________________________________END CALCULATE POLAR COMPLEX____________________________________________________
#________________________________END POLAR COMPLEX NUMBER____________________________________________________

def complex_number():
    """Main Function"""
    print()
    print("COMPLEX NUMBER")
    print()
    print("► Find I^N\t\t► Normal Complex Number\t\t► Polar Complex Number")
    
    print()
    print("What topic do you want to find?: ", end="")
    type_input_set = input().upper()
    if type_input_set == "FIND I^N":
        find_i()
    elif type_input_set == "NORMAL COMPLEX NUMBER":
        normal_complex_number()
    elif type_input_set == "POLAR COMPLEX NUMBER":
        polar_complex_number()
#________________________________END MAIN FUNCTION____________________________________________________

            
