
"""STATISTIC PART1"""
#import แค่ฟังคชันชื่อ statistics1
import statistics
from time import sleep as delay
import sys
def func_again():
    """call_back_fun"""
    print()
    print("Do you want to calculate in this topic again?(Yes/No): ", end="")
    yes_no_back = input().upper()
    if yes_no_back == "YES":
        statistics1()
def mean():
    """MEAN FUNCTION"""
    delay(0.5)
    print("\n")
    print("What Type of MEAN do you want to find?")
    delay(0.5)
    print("► Normal Mean","► Geometric Mean","► Harmonic Mean","► Weighted mean", sep="\n")
    print("Answer: ", end="")
    type_mean = input()
    type_mean = type_mean.upper()

    #_______________________________________________________________NORMAL MEAN__________________________________________________________________________________________
    if type_mean == "NORMAL MEAN":
        delay(0.25)
        print("\n")
        print("Do your data alreay arrange?")
        print("► Yes\t\t\t► No")
        print("Answer: ", end="")
        confirm_mean = input().upper()
        #Normal mean no arrange
        if confirm_mean == "NO":
            print("\n")
            list_data_no_arrnge_mean = []
            delay(0.25)
            print("Input data that you want to calculate (if you want to stop, input \"END\"): ")
            while True:
                input_data_mean = input()
                if input_data_mean == "END":
                    break
                else:
                    try :  
                        float(input_data_mean) 
                        res = True
                    except : 

                        res = False
                    if input_data_mean.isnumeric() or res == True:
                        list_data_no_arrnge_mean.append(float(input_data_mean))
            if list_data_no_arrnge_mean == []:
                print("Please try again and input the data!!!!")
            else:
                answer_no_arrange_mean = statistics.fmean(list_data_no_arrnge_mean)
                print()
                print("Your data mean is %.2f"%(answer_no_arrange_mean))
            func_again()
        #Normal mean with arrange
        elif confirm_mean == "YES":
            print("\n")
            dict_yes_mean = {}
            delay(0.25)
            print("How many vaule in the table?: ", end="")
            vaule_table = int(input())
            for _ in range(vaule_table):
                print("Input vaule: ", end="")
                vaule_ymean = float(input())
                print("Input frequency: ", end="")
                frequen_ymean = int(input())
                dict_yes_mean[vaule_ymean] = frequen_ymean
                print()
            answer_arrange_mean = 0
            divide_arrange_mean = 0
            for i in dict_yes_mean:
                answer_arrange_mean += i*(dict_yes_mean[i])
            for j in dict_yes_mean:
                divide_arrange_mean += dict_yes_mean[j]
            answer_arrange_mean = answer_arrange_mean/divide_arrange_mean
            print()
            print("Your data mean is %.2f"%(answer_arrange_mean))
            func_again()
    #_______________________________________________________________GEOMETRIC MEAN__________________________________________________________________________________________
    elif type_mean == "GEOMETRIC MEAN":
        delay(0.25)
        print("\n")
        print("Input data that you want to calculate (if you want to stop, input \"END\"): ")
        root_gmean = 0
        in_gmean = 1
        list_data_geometric_mean = []
        while True:
                input_data_mean = input()
                if input_data_mean == "END":
                    break
                else:
                    try :  
                        float(input_data_mean) 
                        res = True
                    except : 

                        res = False
                    if input_data_mean.isnumeric() or res == True:
                        list_data_geometric_mean.append(float(input_data_mean))
        if list_data_geometric_mean == []:
            print("Please try again and input the data!!!!")
        else:
            for i in list_data_geometric_mean:
                if i >= 0:
                    in_gmean = in_gmean*i
                root_gmean += 1
            answer_geometric_mean = in_gmean**(1/root_gmean)
            print()
            print("Your data geometric mean is %.2f"%(answer_geometric_mean))
        func_again()

    #_______________________________________________________________HARMONIC MEAN__________________________________________________________________________________________
    elif type_mean == "HARMONIC MEAN":
        delay(0.25)
        print("\n")
        print("Input data that you want to calculate (if you want to stop, input \"END\"): ")
        top_hmean = 0
        bottom_hmean = 0
        list_data_harmonic_mean = []
        while True:
                input_data_mean = input()
                if input_data_mean == "END":
                    break
                else:
                    try :  
                        float(input_data_mean) 
                        res = True
                    except : 

                        res = False
                    if input_data_mean.isnumeric() or res == True:
                        list_data_harmonic_mean.append(float(input_data_mean))
        if list_data_harmonic_mean == []:
            print("Please try again and input the data!!!!")
        else:
            for i in list_data_harmonic_mean:
                if i != 0:
                    bottom_hmean += 1/i
                top_hmean += 1
            if bottom_hmean == 0:
                print("Sorry, your calculate is error T-T")
            else:
                answer_harmonic_mean = top_hmean/bottom_hmean
            print()
            print("Your data harmonic mean is %.2f"%(answer_harmonic_mean))
        func_again()

    #_______________________________________________________________WEIGHTED MEAN__________________________________________________________________________________________
    elif type_mean == "WEIGHTED MEAN":
        delay(0.25)
        print("\n")
        list_vaules_weight_mean = []
        list_weight_weight_mean = []
        divide_weight_mean = 0
        top_weight_mean = 0
        print("Input data of vaule and weight that you want to calculate (if you want to stop, input \"END\" in vaule input): ")
        while True:
            print("Input vaule: ", end="")
            vaule_wmean = input()
            if vaule_wmean == "END":
                break
            else:
                try :  
                    float(vaule_wmean) 
                    res = True
                except : 
                    res = False
                if vaule_wmean.isnumeric() or res == True:
                    list_vaules_weight_mean.append(float(vaule_wmean))
            print("Input weight: ", end="")
            weight_wmean = float(input())
            print()
            list_weight_weight_mean.append(weight_wmean)
        if list_vaules_weight_mean == []:
            print("Please try again and input the data!!!!")
        else:
            for k in range(len(list_vaules_weight_mean)):
                top_weight_mean += list_vaules_weight_mean[k]*list_weight_weight_mean[k]
                divide_weight_mean += list_weight_weight_mean[k]
            if divide_weight_mean == 0:
                print("Sorry, your calculate is error T-T")
            else:
                answer_weight_mean = top_weight_mean/divide_weight_mean
            print()
            print("Your data weighted mean is %.2f"%(answer_weight_mean))
        func_again()
#_______________________________________________________________END MEAN__________________________________________________________________________________________
def med():
    """MEDIAN FUNCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to median finder!")
    delay(0.5)
    print("Do your data alreay arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_median = input().upper()
    if confirm_median == "NO":
            print("\n")
            list_data_median = []
            delay(0.25)
            print("Input data that you want to find median (if you want to stop, input \"END\"): ")
            while True:
                input_data_median = input()
                if input_data_median == "END":
                    break
                else:
                    try :  
                        float(input_data_median) 
                        res = True
                    except : 

                        res = False
                    if input_data_median.isnumeric() or res == True:
                        list_data_median.append(float(input_data_median))
            if list_data_median == []:
                print("Please try again and input the data!!!!")
            else:
                list_data_median.sort()
                answer_median = statistics.median(list_data_median)
                print()
                print("Your data median is %.2f"%(answer_median))
            func_again()
    elif confirm_median == "YES":
        delay(0.25)
        print("\n")
        print("How many range of data?: ", end="")
        range_median = int(input())
        dict_med_arrange = {}
        print("please input the range from small to big")
        for i in range(range_median):
            print()
            print("Input range(Input example \"1-10\"): ", end="")
            range_med_input = input()
            list_range = range_med_input.split("-")
            tuple_range = tuple(list_range)
            print("Input frequency: ", end="")
            frequency_med_input = int(input())
            dict_med_arrange[tuple_range] = frequency_med_input
        median_frequen_sum = sum([dict_med_arrange[x] for x in dict_med_arrange])
        median_frequen_sum_half = median_frequen_sum/2
        check_position = 0
        for j in dict_med_arrange:
            check_position += dict_med_arrange[j]
            if check_position > median_frequen_sum_half:
                list_use_median = j
                break
        lower_med = float(list_use_median[0])-0.5
        width_range = float(list_use_median[1])-float(list_use_median[0])+1
        sum_before_med = 0
        for k in dict_med_arrange:
            if k == list_use_median:
                break
            sum_before_med += dict_med_arrange[k]
        answer_median_arrange = lower_med + (width_range*((median_frequen_sum_half-sum_before_med)/dict_med_arrange[list_use_median]))
        print()
        print("Your data median is %.2f"%(answer_median_arrange))
        func_again()
#_______________________________________________________________END MEDIAN__________________________________________________________________________________________
def mod():
    """MODE FUNCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to mode finder!")
    delay(0.5)
    print("Do your data alreay arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_mode = input().upper()
    if confirm_mode == "NO":
        print("\n")
        list_data_mode = []
        delay(0.25)
        print("Input data that you want to find mode (if you want to stop, input \"END\"): ")
        while True:
            input_data_mode = input()
            if input_data_mode == "END":
                break
            else:
                try :  
                    float(input_data_mode) 
                    res = True
                except : 
                    res = False
                if input_data_mode.isnumeric() or res == True:
                    list_data_mode.append(float(input_data_mode))
        if list_data_mode == []:
            print("Please try again and input the data!!!!")
        else:
            list_data_mode.sort()
            answer_mode = statistics.multimode(list_data_mode)
            print()
            if len(answer_mode) == 1:
                print("Your data mode is %.2f"%(answer_mode[0]))
            elif len(answer_mode) == 2:
                print("Your data mode is %.2f and %.2f"%(answer_mode[0], answer_mode[1]))
            elif len(answer_mode) > 2:
                print("Your data don't have the mode :(")
        func_again()
    elif confirm_mode == "YES":
        delay(0.25)
        print("\n")
        print("How many range of data?: ", end="")
        range_mode = int(input())
        dict_mode_arrange = {}
        print("please input the range from small to big")
        for i in range(range_mode):
            print()
            print("Input range(Input example \"1-10\"): ", end="")
            range_mode_input = input()
            list_rangem = range_mode_input.split("-")
            tuple_rangem = tuple(list_rangem)
            print("Input frequency: ", end="")
            frequency_mode_input = int(input())
            dict_mode_arrange[tuple_rangem] = frequency_mode_input
        check = 0
        for i in dict_mode_arrange:
            width_mode = float(i[1])-float(i[0])+1
            check_max_mode = dict_mode_arrange[i]/width_mode
            if check_max_mode > check:
                tuple_use_mode = i
                check = check_max_mode
        lower_mode = float(tuple_use_mode[0])-0.5
        list_from_dict_mode = list(dict_mode_arrange)
        before_mode = dict_mode_arrange[list_from_dict_mode[list_from_dict_mode.index(tuple_use_mode)-1]]
        try :
            after_mode = dict_mode_arrange[list_from_dict_mode[list_from_dict_mode.index(tuple_use_mode)+1]]
            now_mode = dict_mode_arrange[tuple_use_mode]
            answer_mode_arrange = lower_mode + width_mode*((now_mode-before_mode)/((now_mode-before_mode)+(now_mode-after_mode)))
            
            print()
            print("Your data mode is %.2f"%(answer_mode_arrange))
        except :
            print()
            print("Sorry we can't calculate mode of this data")
            print("Your mode is in the last range")
        func_again()
#_______________________________________________________________END MODE__________________________________________________________________________________________
def statistics1():
    """Main Function"""
    print()
    print("STATISTIC PART1")
    print()
    print("► Mean\t\t\t► Median\t\t\t► Mode")
    print()
    print("What topic do you want to find?: ", end="")
    type_input_stat1 = input().upper()
    if type_input_stat1 == "MEAN":
        mean()
    elif type_input_stat1 == "MEDIAN":
        med()
    elif type_input_stat1 == "MODE":
        mod()

statistics1()    
#_______________________________________________________________END MAIN FUNCTION__________________________________________________________________________________________






                
            
        

