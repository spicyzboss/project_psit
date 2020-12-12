"""SET FUNCTION"""
from time import sleep as delay
import math
import json
#import แค่ฟังคชันชื่อ set_topic()
def func_again():
    """call_back_fun"""
    print()
    print("Do you want to calculate in this topic again?(Yes/No): ", end="")
    yes_no_back = input().upper()
    if yes_no_back == "YES":
        set_topic()

def union_finder():
    """UNION FINDER FUCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Union topic!")
    delay(0.5)
    print()
    print("Which one do you want to find?")
    print("► Find union set\t\t► Find total of union set")
    print("Answer: ", end="")
    type_union = input().upper()
    print()
    if type_union == "FIND UNION SET":
        delay(0.25)
        print("This Topic will find Union set of your input")
        try:
            print()
            union_set_total = int(input("How many set do you want to union?: "))
            print()
            ans_set_union = set({})
            for _ in range(union_set_total):
                set_union = input("Input your set (Input Example \"{1,2,3}\"): ")
                set_union = set_union.replace("{","").replace("}","")
                set_union_list = set_union.split(",")
                set_union_set = set([float(x) for x in set_union_list])
                ans_set_union = ans_set_union.union(set_union_set)
            print()
            if ans_set_union == set():
                print("Your Union set is Blank set")
            else:
                print("Your Union set is %s"%ans_set_union)
                print("Your Union set total is %d"%len(ans_set_union))
        except:
            print("Please IInput in the correct format")
        func_again()
    elif type_union == "FIND TOTAL OF UNION SET":
        delay(0.25)
        print("This Topic will find total of Union set by Formula(2 or 3 sets)")
        print()
        try:
            tunion_set_total = int(input("How many set do you want to find total? (2/3): "))
            print()
            if tunion_set_total == 2:
                aset_union_2 = float(input("Input total of first set: "))
                bset_union_2 = float(input("Input total of second set: "))
                intersect_set_union_2 = float(input("Input total of intersect set: "))
                ans_set_union = aset_union_2+bset_union_2-intersect_set_union_2
            elif tunion_set_total == 3:
                aset_union_3 = float(input("Input total of first set: "))
                bset_union_3 = float(input("Input total of second set: "))
                cset_union_3 = float(input("Input total of third set: "))
                intersect_setab_union_3 = float(input("Input total of intersect of First and Second set: "))
                intersect_setac_union_3 = float(input("Input total of intersect of First and Third set: "))
                intersect_setbc_union_3 = float(input("Input total of intersect of Second and Third set: "))
                intersect_set_union_3 = float(input("Input total of intersect of All set: "))
                ans_set_union = aset_union_3+bset_union_3+cset_union_3-intersect_setab_union_3-intersect_setac_union_3-intersect_setbc_union_3+intersect_set_union_3
            print()
            print("Your Union set total is %d"%ans_set_union)
        except:
            print("Please Input in the correct format")
        func_again()
#_____________________________________END Union______________________________________

def intersect_finder():
    """Intersect FINDER FUCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Intersect topic!")
    delay(0.5)
    print()
    print("Which one do you want to find?")
    print("► Find intersect set\t\t► Check sub set")
    print("Answer: ", end="")
    type_intersect = input().upper()
    print()
    if type_intersect == "FIND INTERSECT SET":
        delay(0.25)
        print("This Topic will find Intersect set of your input")
        print()
        try:
            intersect_set_total = int(input("How many set do you want to intersect?: "))
            print()
            check = 1
            ans_set_intersect = set({})
            for _ in range(intersect_set_total):
                if check == 1:
                    set_intersect = input("Input your set (Input Example \"{1,2,3}\"): ")
                    set_intersect = set_intersect.replace("{","").replace("}","")
                    set_intersect_list = set_intersect.split(",")
                    set_intersect_set = set([float(x) for x in set_intersect_list])
                    ans_set_intersect = ans_set_intersect.union(set_intersect_set)
                else:
                    set_intersect = input("Input your set (Input Example \"{1,2,3}\"): ")
                    set_intersect = set_intersect.replace("{","").replace("}","")
                    set_intersect_list = set_intersect.split(",")
                    set_intersect_set = set([float(x) for x in set_intersect_list])
                    ans_set_intersect = ans_set_intersect.intersection(set_intersect_set)
                check += 1
            print()
            if ans_set_intersect == set():
                print("Your Intersect set is Blank set")
            else:
                print("Your intersect set is %s"%ans_set_intersect)
                print("Your intersect set total is %d"%len(ans_set_intersect))
        except:
            print("Please Input in the correct format")
        func_again()
    elif type_intersect == "CHECK SUB SET":
        delay(0.25)
        print("This Topic will check does B set is sub set of A set?")
        print()
        try:
            aset_sub = input("Input A set(Input Example \"{1,2,3}\"): ")
            bset_sub = input("Input B set(Input Example \"{1,2,3}\"): ")
            set_a_sub = aset_sub.replace("{","").replace("}","")
            set_a_sub_list = set_a_sub.split(",")
            set_a_sub_set = set([float(x) for x in set_a_sub_list])
            set_b_sub = bset_sub.replace("{","").replace("}","")
            set_b_sub_list = set_b_sub.split(",")
            set_b_sub_set = set([float(x) for x in set_b_sub_list])
            ans_sub = set_b_sub_set.issubset(set_a_sub_set)
            if ans_sub == True:
                print()
                print("%s is sub set of %s"%(bset_sub, aset_sub))
            else:
                print()
                print("%s is not sub set of %s"%(bset_sub, aset_sub))
        except:
            print("Please Input in the correct format")  
        func_again()
#_____________________________________END INTERSECT______________________________________

def difference_finder():
    """DIFFERENCE FINDER FUCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Difference topic!")
    delay(0.5)
    print()
    print("Which one do you want to find?")
    print("► Difference your main set\t\t► Find symmetric difference set")
    print("Answer: ", end="")
    type_difference = input().upper()
    print()
    if type_difference == "DIFFERENCE YOUR MAIN SET":
        delay(0.25)
        print("This Topic will find Main set after difference by your input")
        print()
        try:
            main_set_dif = input("Input your Main Set (Input Example \"{1,2,3}\"): ")
            set_difference_main = main_set_dif.replace("{","").replace("}","")
            set_difference_list_main = set_difference_main.split(",")
            ans_set_difference = set([float(x) for x in set_difference_list_main])
            print()
            difference_set_total = int(input("How many set do you want to difference from main set?: "))
            print()
            for _ in range(difference_set_total):
                set_difference = input("Input your set (Input Example \"{1,2,3}\"): ")
                set_difference = set_difference.replace("{","").replace("}","")
                set_difference_list = set_difference.split(",")
                set_difference_set = set([float(x) for x in set_difference_list])
                ans_set_difference = ans_set_difference.difference(set_difference_set)
            print()
            if ans_set_difference == set():
                print("Your Main set is Blank set")
            else:
                print("Your Main set after difference is %s"%ans_set_difference)
                print("Your Main set total is %d"%len(ans_set_difference))
        except:
            print("Please Input in the correct format")
        func_again()
    elif type_difference == "FIND SYMMETRIC DIFFERENCE SET":
        delay(0.25)
        print("This Topic will find Set after delete intersect")
        print()
        try:
            symdifference_set_total = int(input("How many set do you want to find Symmetric symdifference set?: "))
            print()
            ans_set_symdifference = set({})
            for _ in range(symdifference_set_total):
                set_symdifference = input("Input your set (Input Example \"{1,2,3}\"): ")
                set_symdifference = set_symdifference.replace("{","").replace("}","")
                set_symdifference_list = set_symdifference.split(",")
                set_symdifference_set = set([float(x) for x in set_symdifference_list])
                ans_set_symdifference = ans_set_symdifference.symmetric_difference(set_symdifference_set)
            print()
            if ans_set_symdifference == set():
                print("Your Symmetric Different set is Blank set")
            else:
                print("Your Symmetric Different set after symdifference is %s"%ans_set_symdifference)
                print("Your Symmetric Different set total is %d"%len(ans_set_symdifference))
        except:
            print("Please Input in the correct format")
        func_again()
#_____________________________________END DIFFERENCE______________________________________
def set_topic():
    """Main Function"""
    print()
    print("SET")
    print()
    print("► Union\t\t► Intersect\t\t► Difference")
    
    print()
    print("What topic do you want to find?: ", end="")
    type_input_set = input().upper()
    if type_input_set == "UNION":
        union_finder()
    elif type_input_set == "INTERSECT":
        intersect_finder()
    elif type_input_set == "DIFFERENCE":
        difference_finder()
set_topic()
#_____________________________________END MAIN FUNCTION______________________________________
