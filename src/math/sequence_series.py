"""SEQUENCE & SERIE"""
from time import sleep as delay
import math
#import แค่ฟังคชันชื่อ sequence_sigma_series()

def sequence():
    """FIND N TERM FROM ARITHMETRIC AND GEOMETRIC SEQUENCE"""
    delay(0.5)
    print("Welcome to Sequence topic!")
    delay(0.5)
    print()
    print("Which Sequence do you want to find?")
    print("► Arithmetic sequence\t\t► Geometric sequence")
    print("Answer: ", end="")
    type_sequence = input().upper()
    print()
    if type_sequence == "ARITHMETIC SEQUENCE":
        delay(0.25)
        print("This Topic will find N term of the Arimethic Sequence")
        print()
        print("Input First data of Sequence: ", end="")
        first_arimethic = float(input())
        print("Input Number of term of Sequence: ", end="")
        number_arimethic = float(input())
        print("Input Common difference of Sequence: ", end="")
        diff_arimethic = float(input())
        print()
        ans_arimethic = first_arimethic+((number_arimethic-1)*diff_arimethic)
        print("The %d term of Sequence is %.2f"%(number_arimethic, ans_arimethic))

    elif type_sequence == "GEOMETRIC SEQUENCE":
        delay(0.25)
        print("This Topic will find N term of the Geometric Sequence")
        print()
        print("Input First data of Sequence: ", end="")
        first_geometric = float(input())
        print("Input Number of term of Sequence: ", end="")
        number_geometric = float(input())
        print("Input Common ratio of Sequence: ", end="")
        rat_geometric = float(input())
        print()
        ans_geometric = first_geometric*(rat_geometric**(number_geometric-1))
        print("The %d term of Sequence is %.2f"%(number_geometric, ans_geometric))

#_____________________________________END SEQUENCE______________________________________
def sigma():
    """FIND SUM OF 1toN 1^2toN^2 and 1^3toN^3"""
    delay(0.5)
    print("Welcome to Sigma topic!")
    delay(0.5)
    print()
    print("Which form of i do you want to find? (\"^\" mean Exponential)")
    print("► i\t\t► i^2\t\t► i^3")
    print("Answer: ", end="")
    type_sigma = input().upper()
    print()
    if type_sigma == "I":
        delay(0.25)
        print("This form will find the sum of 1+2+3+...+N")
        print()
        print("Input the N term of sigma: ", end="")
        n_sigma = float(input())
        ans_sigma_i = (n_sigma*(n_sigma+1))/2
        print()
        print("The Summation of 1 to %d is %.2f"%(n_sigma, ans_sigma_i))

    elif type_sigma == "I^2":
        delay(0.25)
        print("This form will find the sum of 1^2+2^2+3^2+...+N^2 (\"^\" mean Exponential)")
        print()
        print("Input the N term of sigma: ", end="")
        n_sigma_2 = float(input())
        ans_sigma_i2 = (n_sigma_2*(n_sigma_2+1)*(2*n_sigma_2+1))/6
        print()
        print("The Summation of 1^2 to %d^2 is %.2f"%(n_sigma_2, ans_sigma_i2))

    elif type_sigma == "I^3":
        delay(0.25)
        print("This form will find the sum of 1^3+2^3+3^3+...+N^3 (\"^\" mean Exponential)")
        print()
        print("Input the N term of sigma: ", end="")
        n_sigma_3 = float(input())
        ans_sigma_i3 = ((n_sigma_3*(n_sigma_3+1))/2)**2
        print()
        print("The Summation of 1^3 to %d^3 is %.2f"%(n_sigma_3, ans_sigma_i3))

#_____________________________________END SIGMA______________________________________
def series():
    """Find series of arithmetic and geometric"""
    delay(0.5)
    print("Welcome to Series topic!")
    delay(0.5)
    print()
    print("Which Series do you want to find?")
    print("► Arithmetic series\t\t► Geometric series")
    print("Answer: ", end="")
    type_series = input().upper()
    print()
    if type_series == "ARITHMETIC SERIES":
        delay(0.25)
        print("Which Arithmetic Series do you want to find?")
        print("► Normal\t\t► Infinite")
        print("Answer: ", end="")
        type_ari_series = input().upper()
        print()
        if type_ari_series == "NORMAL":
            delay(0.25)
            print("This topic will find N term of Arithmetic Series")
            print()
            print("Input First data of Series: ", end="")
            first_arimethic_series = float(input())
            print("Input Number of term of Series: ", end="")
            number_arimethic_series = float(input())
            print("Input Common difference of Series: ", end="")
            diff_arimethic_series = float(input())
            print()
            ans_arith_series = (number_arimethic_series/2)*((2*first_arimethic_series)+((number_arimethic_series-1)*diff_arimethic_series))
            print()
            print("The %d term of Series is %.2f"%(number_arimethic_series, ans_arith_series))

        elif type_ari_series == "INFINITE":
            delay(0.25)
            print("This topic will find infinite term of Arithmetic Series")
            print()
            print("Input First data of Series: ", end="")
            first_arimethic_series = float(input())
            print("Input Common difference of Series: ", end="")
            diff_arimethic_series = float(input())
            print()
            if first_arimethic_series == 0 and diff_arimethic_series == 0:
                print("The infinite term of this Series is 0(Convergent Series)")
            else:
                print("This Series can't find Infinite term(Divergent Series)")

    elif type_series == "GEOMETRIC SERIES":
        delay(0.25)
        print("Which Geometric Series do you want to find?")
        print("► Normal\t\t► Infinite")
        print("Answer: ", end="")
        type_geo_series = input().upper()
        print()
        if type_geo_series == "NORMAL":
            delay(0.25)
            print("This topic will find N term of Geometric Series")
            print()
            print("Input First data of Series: ", end="")
            first_geometric_series = float(input())
            print("Input Number of term of Series: ", end="")
            number_geometric_series = float(input())
            print("Input Common ratio of Series: ", end="")
            rat_geometric_series = float(input())
            print()
            if rat_geometric_series > 1:
                ans_geo_series = (first_geometric_series*((rat_geometric_series**number_geometric_series)-1))/(rat_geometric_series-1)
            elif rat_geometric_series == 1:
                ans_geo_series = number_geometric_series*first_geometric_series
            elif rat_geometric_series < 1:
                ans_geo_series = (first_geometric_series*(1-(rat_geometric_series**number_geometric_series)))/(1-rat_geometric_series)
            print()
            print("The %d term of Series is %.2f"%(number_geometric_series, ans_geo_series))

        elif type_geo_series == "INFINITE":
            delay(0.25)
            print("This topic will find infinite term of Geometric Series")
            print()
            print("Input First data of Series: ", end="")
            first_geometric_series = float(input())
            print("Input Common ratio of Series: ", end="")
            rat_geometric_series = float(input())
            print()
            if -1 < rat_geometric_series < 1:
                ans_geo_series = first_geometric_series/(1-rat_geometric_series)
                print("The infinite term of this Series is %.2f(Convergent Series)"%(ans_geo_series))
            else:
                print("This Series can't find Infinite term(Divergent Series)")

#_____________________________________END SERIES______________________________________

def sequence_sigma_series():
    """Main Function"""
    print("SEQUENCE & SIGMA & SERIES\n")
    print("► Sequence\t\t► Sigma\t\t► Series\n")
    print("What topic do you want to find?: ", end="")
    type_input_3s = input().upper()
    if type_input_3s == "SEQUENCE":
        sequence()
    elif type_input_3s == "SIGMA":
        sigma()
    elif type_input_3s == "SERIES":
        series()

#_____________________________________END MAIN FUNCTION______________________________________
