
"""STATISTIC PART2"""
#import แค่ฟังคชันชื่อ statistics2
import statistics
from time import sleep as delay
import math

def func_again():
    """call_back_fun"""
    print()
    print("Do you want to calculate in this topic again?(Yes/No): ", end="")
    yes_no_back = input().upper()
    if yes_no_back == "YES":
        statistics2()

def relative_position():
    """RELATIVE POSITION FUCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Relative Position topic!")
    delay(0.5)
    print("Do your data already arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_rp = input().upper()
    if confirm_rp == "NO":
        print()
        print("Which Relative Position do you want to find?")
        print("► Quartile\t\t\t► Decile\t\t\t► Percentile")
        print("Answer: ", end="")
        type_rp_noarrange = input().upper()
    #_______________________________________QUARTILE No arrange_________________________
        if type_rp_noarrange == "QUARTILE":
            print("\n")
            print("Input quartile that you want to find(1-4): ", end="")
            qrp_type_noarrange = int(input())
            print()
            list_data_qrp = []
            delay(0.25)
            print("Input data that you want to find quatile (if you want to stop, input \"END\"): ")
            while True:
                input_data_qrp = input()
                if input_data_qrp == "END":
                    break
                else:
                    try :  
                        float(input_data_qrp) 
                        res = True
                    except : 
                        res = False
                    if input_data_qrp.isnumeric() or res == True:
                        list_data_qrp.append(float(input_data_qrp))
            if list_data_qrp == []:
                print("Please try again and input the data!!!!")
            else:
                list_data_qrp.sort()
                position_qrp_no = (qrp_type_noarrange*(len(list_data_qrp)+1))/4
                after_numqrp = list_data_qrp[int(position_qrp_no//1)]
                before_numqrp = list_data_qrp[int(position_qrp_no//1-1)]
                answer_qrp_noa = ((after_numqrp-before_numqrp)*(position_qrp_no-(position_qrp_no//1)))+before_numqrp
                print("Your data %s quartile is %.2f"%(qrp_type_noarrange, answer_qrp_noa))
            func_again()
    #_______________________________________Decile No arrange_________________________
        elif type_rp_noarrange == "DECILE":
            print("\n")
            print("Input decile that you want to find(1-10): ", end="")
            drp_type_noarrange = int(input())
            print()
            list_data_drp = []
            delay(0.25)
            print("Input data that you want to find decile (if you want to stop, input \"END\"): ")
            while True:
                input_data_drp = input()
                if input_data_drp == "END":
                    break
                else:
                    try :  
                        float(input_data_drp) 
                        res = True
                    except : 
                        res = False
                    if input_data_drp.isnumeric() or res == True:
                        list_data_drp.append(float(input_data_drp))
            if list_data_drp == []:
                print("Please try again and input the data!!!!")
            else:
                list_data_drp.sort()
                position_drp_no = (drp_type_noarrange*(len(list_data_drp)+1))/10
                after_numdrp = list_data_drp[int(position_drp_no//1)]
                before_numdrp = list_data_drp[int(position_drp_no//1-1)]
                answer_drp_noa = ((after_numdrp-before_numdrp)*(position_drp_no-(position_drp_no//1)))+before_numdrp
                print("Your data %s quartile is %.2f"%(drp_type_noarrange, answer_drp_noa))
            func_again()
    #_______________________________________Percentile No arrange_________________________
        elif type_rp_noarrange == "PERCENTILE":
            print("\n")
            print("Input percentile that you want to find(1-100): ", end="")
            prp_type_noarrange = int(input())
            print()
            list_data_prp = []
            delay(0.25)
            print("Input data that you want to find percentile (if you want to stop, input \"END\"): ")
            while True:
                input_data_prp = input()
                if input_data_prp == "END":
                    break
                else:
                    try :  
                        float(input_data_prp) 
                        res = True
                    except : 
                        res = False
                    if input_data_prp.isnumeric() or res == True:
                        list_data_prp.append(float(input_data_prp))
            if list_data_prp == []:
                print("Please try again and input the data!!!!")
            else:
                list_data_prp.sort()
                position_prp_no = (prp_type_noarrange*(len(list_data_prp)+1))/100
                after_numprp = list_data_prp[int(position_prp_no//1)]
                before_numprp = list_data_prp[int(position_prp_no//1-1)]
                answer_prp_noa = ((after_numprp-before_numprp)*(position_prp_no-(position_prp_no//1)))+before_numprp
                print("Your data %s percentile is %.2f"%(prp_type_noarrange, answer_prp_noa))
            func_again()
    elif confirm_rp == "YES":
        print()
        print("Which Relative Position do you want to find?")
        print("► Quartile\t\t\t► Decile\t\t\t► Percentile")
        print("Answer: ", end="")
        type_rp_arrange = input().upper()
        #_______________________________________Quartile arrange_________________________________________________________________
        if type_rp_arrange == "QUARTILE":
            delay(0.25)
            print("\n")
            print("Input quartile that you want to find(1-4): ", end="")
            qrp_type_arrange = int(input())
            print()
            print("How many range of data?: ", end="")
            range_qrp_arrange = int(input())
            dict_qrp_arrange = {}
            print("please input the range from small to big")
            for i in range(range_qrp_arrange):
                print()
                print("Input range(Input example \"1-10\"): ", end="")
                range_qrp_input = input()
                list_range_qrp = range_qrp_input.split("-")
                tuple_range = tuple(list_range_qrp)
                print("Input frequency: ", end="")
                frequency_qrp_input = int(input())
                dict_qrp_arrange[tuple_range] = frequency_qrp_input
            qrp_frequen_sum = sum([dict_qrp_arrange[x] for x in dict_qrp_arrange])
            qrp_position_frequency = (qrp_frequen_sum*qrp_type_arrange)/4
            check_position = 0
            for j in dict_qrp_arrange:
                check_position += dict_qrp_arrange[j]
                if check_position > qrp_position_frequency:
                    list_use_qrp = j
                    break
            lower_qrp = float(list_use_qrp[0])-0.5
            width_range = float(list_use_qrp[1])-float(list_use_qrp[0])+1
            sum_before_qrp = 0
            for k in dict_qrp_arrange:
                if k == list_use_qrp:
                    break
                sum_before_qrp += dict_qrp_arrange[k]
            answer_qrp_arrange = lower_qrp + (width_range*((qrp_position_frequency-sum_before_qrp)/dict_qrp_arrange[list_use_qrp]))
            print()
            print("Your data %s quartile is %.2f"%(qrp_type_arrange, answer_qrp_arrange))
            func_again()
        #_______________________________________Decile arrange_________________________________________________________________
        elif type_rp_arrange == "DECILE":
            delay(0.25)
            print("\n")
            print("Input decile that you want to find(1-10): ", end="")
            drp_type_arrange = int(input())
            print()
            print("How many range of data?: ", end="")
            range_drp_arrange = int(input())
            dict_drp_arrange = {}
            print("please input the range from small to big")
            for i in range(range_drp_arrange):
                print()
                print("Input range(Input example \"1-10\"): ", end="")
                range_drp_input = input()
                list_range_drp = range_drp_input.split("-")
                tuple_range = tuple(list_range_drp)
                print("Input frequency: ", end="")
                frequency_drp_input = int(input())
                dict_drp_arrange[tuple_range] = frequency_drp_input
            drp_frequen_sum = sum([dict_drp_arrange[x] for x in dict_drp_arrange])
            drp_position_frequency = (drp_frequen_sum*drp_type_arrange)/10
            check_position = 0
            for j in dict_drp_arrange:
                check_position += dict_drp_arrange[j]
                if check_position > drp_position_frequency:
                    list_use_drp = j
                    break
            lower_drp = float(list_use_drp[0])-0.5
            width_range = float(list_use_drp[1])-float(list_use_drp[0])+1
            sum_before_drp = 0
            for k in dict_drp_arrange:
                if k == list_use_drp:
                    break
                sum_before_drp += dict_drp_arrange[k]
            answer_drp_arrange = lower_drp + (width_range*((drp_position_frequency-sum_before_drp)/dict_drp_arrange[list_use_drp]))
            print()
            print("Your data %s decile is %.2f"%(drp_type_arrange, answer_drp_arrange))
            func_again()
        #_______________________________________Percentile arrange_________________________________________________________________
        elif type_rp_arrange == "PERCENTILE":
            delay(0.25)
            print("\n")
            print("Input percentile that you want to find(1-100): ", end="")
            prp_type_arrange = int(input())
            print()
            print("How many range of data?: ", end="")
            range_prp_arrange = int(input())
            dict_prp_arrange = {}
            print("please input the range from small to big")
            for i in range(range_prp_arrange):
                print()
                print("Input range(Input example \"1-10\"): ", end="")
                range_prp_input = input()
                list_range_prp = range_prp_input.split("-")
                tuple_range = tuple(list_range_prp)
                print("Input frequency: ", end="")
                frequency_prp_input = int(input())
                dict_prp_arrange[tuple_range] = frequency_prp_input
            prp_frequen_sum = sum([dict_prp_arrange[x] for x in dict_prp_arrange])
            prp_position_frequency = (prp_frequen_sum*prp_type_arrange)/100
            check_position = 0
            for j in dict_prp_arrange:
                check_position += dict_prp_arrange[j]
                if check_position > prp_position_frequency:
                    list_use_prp = j
                    break
            lower_prp = float(list_use_prp[0])-0.5
            width_range = float(list_use_prp[1])-float(list_use_prp[0])+1
            sum_before_prp = 0
            for k in dict_prp_arrange:
                if k == list_use_prp:
                    break
                sum_before_prp += dict_prp_arrange[k]
            answer_prp_arrange = lower_prp + (width_range*((prp_position_frequency-sum_before_prp)/dict_prp_arrange[list_use_prp]))
            print()
            print("Your data %s percentile is %.2f"%(prp_type_arrange, answer_prp_arrange))
            func_again()
#_______________________________________END RELATIVE POSITION_________________________________________________________________
def range_finder():
    delay(0.5)
    print("\n")
    print("Welcome to Range and Coefficient of Range topic!")
    delay(0.5)
    print("Do your data already arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_range = input().upper()
    if confirm_range == "NO":
        print()
        list_data_range = []
        delay(0.25)
        print("Input data that you want to find range and coefficient of range (if you want to stop, input \"END\"): ")
        while True:
            input_data_range = input()
            if input_data_range == "END":
                break
            else:
                try :  
                    float(input_data_range) 
                    res = True
                except : 
                    res = False
                if input_data_range.isnumeric() or res == True:
                    list_data_range.append(float(input_data_range))
        if list_data_range == []:
            print("Please try again and input the data!!!!")
        else:
            answer_range_noarrange = max(list_data_range)-min(list_data_range)
            answer2_range_noarrange = max(list_data_range)+min(list_data_range)
            print()
            print("Your data range is %.2f"%(answer_range_noarrange))
            print("Your data coefficient of range is %.2f"%(answer_range_noarrange/answer2_range_noarrange))
        func_again()
    elif confirm_range == "YES":
        print()
        delay(0.25)
        print("Input the lowest range of data(Input example \"1-10\"): ", end="")
        range_arrangelow_input = input()
        list_arrangelow_range = range_arrangelow_input.split("-")
        print("Input the highest range of data(Input example \"1-10\"): ", end="")
        range_arrangehigh_input = input()
        list_arrangehigh_range = range_arrangehigh_input.split("-")
        answer_arrange_range = (float(list_arrangehigh_range[1])+0.5)-(float(list_arrangelow_range[0])-0.5)
        answer2_arrange_range = (float(list_arrangehigh_range[1])+0.5)+(float(list_arrangelow_range[0])-0.5)
        print()
        print("Your data range is %.2f"%(answer_arrange_range))
        print("Your data coefficient of range is %.2f"%(answer_arrange_range/answer2_arrange_range))
        func_again()
#_______________________________________END RANGE_______________________________________________________________________________________________________
def quartile_no(listquartile,quartilenum):
    """QUARTION FUNCTION FOR QD"""
    listquartile.sort()
    position_qrp_no = (quartilenum*(len(listquartile)+1))/4
    after_numqrp = listquartile[int(position_qrp_no//1)]
    before_numqrp = listquartile[int(position_qrp_no//1-1)]
    answer_qrp_noa = ((after_numqrp-before_numqrp)*(position_qrp_no-(position_qrp_no//1)))+before_numqrp
    return answer_qrp_noa
def quartilearrange(dict_qrp_arrange, qrp_type_arrange):
    """QUARTION FUNCTION FOR QD"""
    qrp_frequen_sum = sum([dict_qrp_arrange[x] for x in dict_qrp_arrange])
    qrp_position_frequency = (qrp_frequen_sum*qrp_type_arrange)/4
    check_position = 0
    for j in dict_qrp_arrange:
        check_position += dict_qrp_arrange[j]
        if check_position > qrp_position_frequency:
            list_use_qrp = j
            break
    lower_qrp = float(list_use_qrp[0])-0.5
    width_range = float(list_use_qrp[1])-float(list_use_qrp[0])+1
    sum_before_qrp = 0
    for k in dict_qrp_arrange:
        if k == list_use_qrp:
            break
        sum_before_qrp += dict_qrp_arrange[k]
    answer_qrp_arrange = lower_qrp + (width_range*((qrp_position_frequency-sum_before_qrp)/dict_qrp_arrange[list_use_qrp]))
    return answer_qrp_arrange
def quartile_deviation():
    """QUARTILE DEVIATION FUNCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Quartile Deviation and its Coefficient topic!")
    delay(0.5)
    print("Do your data already arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_qdv = input().upper()
    if confirm_qdv == "NO":
        print("\n")
        list_data_qdv = []
        delay(0.25)
        print("Input data that you want to find quatile deviation and coefficient (if you want to stop, input \"END\"): ")
        while True:
            input_data_qdv = input()
            if input_data_qdv == "END":
                break
            else:
                try :  
                    float(input_data_qdv) 
                    res = True
                except : 
                    res = False
                if input_data_qdv.isnumeric() or res == True:
                    list_data_qdv.append(float(input_data_qdv))
        if list_data_qdv == []:
            print("Please try again and input the data!!!!")
        else:
            answer_noarrange_qdv = (quartile_no(list_data_qdv, 3)-quartile_no(list_data_qdv, 1))/2
            answer2_noarrange_qdv = (quartile_no(list_data_qdv, 3)-quartile_no(list_data_qdv, 1))/(quartile_no(list_data_qdv, 3)+quartile_no(list_data_qdv, 1))
            print()
            print("Your data quartile deviation is %.2f"%(answer_noarrange_qdv))
            print("Your data quartile deviation coefficient is %.2f"%(answer2_noarrange_qdv))
        func_again()
    elif confirm_qdv == "YES":
        delay(0.25)
        print("\n")
        print("How many range of data?: ", end="")
        range_qdv_arrange = int(input())
        dict_qdv_arrange = {}
        print("please input the range from small to big")
        for i in range(range_qdv_arrange):
            print()
            print("Input range(Input example \"1-10\"): ", end="")
            range_qdv_input = input()
            list_range_qdv = range_qdv_input.split("-")
            tuple_range = tuple(list_range_qdv)
            print("Input frequency: ", end="")
            frequency_qdv_input = int(input())
            dict_qdv_arrange[tuple_range] = frequency_qdv_input
        answer_arrange_qdv = (quartilearrange(dict_qdv_arrange, 3)-quartilearrange(dict_qdv_arrange, 1))/2
        answer2_arrange_qdv = (quartilearrange(dict_qdv_arrange, 3)-quartilearrange(dict_qdv_arrange, 1))/(quartilearrange(dict_qdv_arrange, 3)+quartilearrange(dict_qdv_arrange, 1))
        print()
        print("Your data quartile deviation is %.2f"%(answer_arrange_qdv))
        print("Your data quartile deviation coefficient is %.2f"%(answer2_arrange_qdv))
        func_again()
#_______________________________________END QUARTILE DEVIATION_________________________________________________________________
def mean_deviation():
    """MEAN DEVIATION FUCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Mean Deviation and its Coefficient topic!")
    delay(0.5)
    print("Do your data already arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_mdv = input().upper()
    if confirm_mdv == "NO":
        print("\n")
        list_data_mdv = []
        delay(0.25)
        print("Input data that you want to find mean deviation (if you want to stop, input \"END\"): ")
        while True:
            input_data_mdv = input()
            if input_data_mdv == "END":
                break
            else:
                try :  
                    float(input_data_mdv) 
                    res = True
                except : 
                    res = False
                if input_data_mdv.isnumeric() or res == True:
                    list_data_mdv.append(float(input_data_mdv))
        if list_data_mdv == []:
            print("Please try again and input the data!!!!")
        else:
            mean_noarrange_mdv = statistics.fmean(list_data_mdv)
            answer_noarrange_mdv = 0
            for i in list_data_mdv:
                answer_noarrange_mdv += abs(i-mean_noarrange_mdv)
            print()
            print("Your data mean deviation is %.2f"%(answer_noarrange_mdv/len(list_data_mdv)))
            print("Your data mean deviation coefficient is %.2f"%((answer_noarrange_mdv/len(list_data_mdv))/mean_noarrange_mdv))
        func_again()
    elif confirm_mdv == "YES":
        print("\n")
        dict_yes_mdv = {}
        delay(0.25)
        print("How many vaule in the table?: ", end="")
        vaule_table = int(input())
        for _ in range(vaule_table):
            print("Input vaule: ", end="")
            vaule_ymdv = float(input())
            print("Input frequency: ", end="")
            frequen_ymdv = int(input())
            dict_yes_mdv[vaule_ymdv] = frequen_ymdv
            print()
        answer_arrange_mdv = 0
        divide_arrange_mdv = 0
        for i in dict_yes_mdv:
            answer_arrange_mdv += i*(dict_yes_mdv[i])
        for j in dict_yes_mdv:
            divide_arrange_mdv += dict_yes_mdv[j]
        mean_arrange_mdv = answer_arrange_mdv/divide_arrange_mdv
        answer_arrange_mdv = 0
        for k in dict_yes_mdv:
            answer_arrange_mdv += dict_yes_mdv[k]*(abs(k-mean_arrange_mdv))
        print()
        print("Your data mean deviation is %.2f"%(answer_arrange_mdv/divide_arrange_mdv))
        print("Your data mean deviation coefficient is %.2f"%((answer_arrange_mdv/divide_arrange_mdv)/mean_arrange_mdv))
        func_again()
#_______________________________________END MEAN DEVIATION_________________________________________________________________

def standard_deviation():
    """STANDARD DEVIATION FUCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Standard Deviation and its Coefficient topic!")
    delay(0.5)
    print("Do your data already arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_sdv = input().upper()
    if confirm_sdv == "NO":
        print("\n")
        list_data_sdv = []
        delay(0.25)
        print("Input data that you want to find standard deviation and Coefficient (if you want to stop, input \"END\"): ")
        while True:
            input_data_sdv = input()
            if input_data_sdv == "END":
                break
            else:
                try :  
                    float(input_data_sdv) 
                    res = True
                except : 
                    res = False
                if input_data_sdv.isnumeric() or res == True:
                    list_data_sdv.append(float(input_data_sdv))
        if list_data_sdv == []:
            print("Please try again and input the data!!!!")
        else:
            sum_expo2_sdv = 0
            sum_sdv = 0
            all_num_sdv = len(list_data_sdv)
            for i in list_data_sdv:
                sum_expo2_sdv += i**2
                sum_sdv += i
            answer_noarrange_sdv = math.sqrt(((all_num_sdv*sum_expo2_sdv)-sum_sdv**2)/(all_num_sdv*(all_num_sdv-1)))
            print()
            print("Your data standard deviation is %.2f"%(answer_noarrange_sdv))
            print("Your data standard deviation coefficient is %.2f"%(answer_noarrange_sdv/(sum_sdv/all_num_sdv)))
        func_again()
    elif confirm_sdv == "YES":
        delay(0.25)
        print("\n")
        print("How many range of data?: ", end="")
        range_sdv = int(input())
        dict_yes_sdv = {}
        print("please input the range from small to big")
        for i in range(range_sdv):
            print()
            print("Input range(Input example \"1-10\"): ", end="")
            range_sdv_input = input()
            list_range = range_sdv_input.split("-")
            middle_sdv = (float(list_range[0])+float(list_range[1]))/2
            print("Input frequency: ", end="")
            frequency_sdv_input = int(input())
            dict_yes_sdv[middle_sdv] = frequency_sdv_input
        mean_svd_arrange = sum([x*dict_yes_sdv[x] for x in dict_yes_sdv])/sum([dict_yes_sdv[x] for x in dict_yes_sdv])
        sum_expo2_sdv_arrange =sum([dict_yes_sdv[y]*(y**2) for y in dict_yes_sdv])
        all_num_sdv_arrange = sum([dict_yes_sdv[x] for x in dict_yes_sdv])
        answer_arrange_sdv = math.sqrt((all_num_sdv_arrange*sum_expo2_sdv_arrange-(mean_svd_arrange**2))/(all_num_sdv_arrange*(all_num_sdv_arrange-1)))
            
        print()
        print("Your data standard deviation is %.2f"%(answer_arrange_sdv))
        print("Your data standard deviation coefficient is %.2f"%(answer_arrange_sdv/mean_svd_arrange))
        func_again()
#_______________________________________END STANDARD DEVIATION_________________________________________________________________

def variance():
    """VARIANCE FUCTION"""
    delay(0.5)
    print("\n")
    print("Welcome to Variance topic!")
    delay(0.5)
    print("Do your data already arrange?")
    print("► Yes\t\t\t► No")
    print("Answer: ", end="")
    confirm_variance = input().upper()
    if confirm_variance == "NO":
        print("\n")
        list_data_variance = []
        delay(0.25)
        print("Input data that you want to find standard deviation (if you want to stop, input \"END\"): ")
        while True:
            input_data_variance = input()
            if input_data_variance == "END":
                break
            else:
                try :  
                    float(input_data_variance) 
                    res = True
                except : 
                    res = False
                if input_data_variance.isnumeric() or res == True:
                    list_data_variance.append(float(input_data_variance))
        if list_data_variance == []:
            print("Please try again and input the data!!!!")
        else:
            sum_expo2_variance = 0
            sum_variance = 0
            all_num_variance = len(list_data_variance)
            for i in list_data_variance:
                sum_expo2_variance += i**2
                sum_variance += i
            answer_noarrange_variance = ((all_num_variance*sum_expo2_variance)-sum_variance**2)/(all_num_variance*(all_num_variance-1))
            print()
            print("Your data variance is %.2f"%(answer_noarrange_variance))
        func_again()
    elif confirm_variance == "YES":
        delay(0.25)
        print("\n")
        print("How many range of data?: ", end="")
        range_variance = int(input())
        dict_yes_variance = {}
        print("please input the range from small to big")
        for i in range(range_variance):
            print()
            print("Input range(Input example \"1-10\"): ", end="")
            range_variance_input = input()
            list_range = range_variance_input.split("-")
            middle_variance = (float(list_range[0])+float(list_range[1]))/2
            print("Input frequency: ", end="")
            frequency_variance_input = int(input())
            dict_yes_variance[middle_variance] = frequency_variance_input
        mean_svd_arrange = sum([x*dict_yes_variance[x] for x in dict_yes_variance])/sum([dict_yes_variance[x] for x in dict_yes_variance])
        sum_expo2_variance_arrange =sum([dict_yes_variance[y]*(y**2) for y in dict_yes_variance])
        all_num_variance_arrange = sum([dict_yes_variance[x] for x in dict_yes_variance])
        answer_arrange_variance = (all_num_variance_arrange*sum_expo2_variance_arrange-(mean_svd_arrange**2))/(all_num_variance_arrange*(all_num_variance_arrange-1))
            
        print()
        print("Your data variance is %.2f"%(answer_arrange_variance))
        func_again()
#_______________________________________END VARIANCE_________________________________________________________________

def statistics2():
    """Main Function"""
    print()
    print("STATISTIC PART2")
    print()
    print("► Relative Position\t► Range\t\t\t► Quartile Deviation")
    print("► Mean Deviation\t► Standard Deviation\t► Variance")
    print()
    print("What topic do you want to find?: ", end="")
    type_input_stat2 = input().upper()
    if type_input_stat2 == "RELATIVE POSITION":
        relative_position()
    elif type_input_stat2 == "RANGE":
        range_finder()
    elif type_input_stat2 == "QUARTILE DEVIATION":
        quartile_deviation()
    elif type_input_stat2 == "MEAN DEVIATION":
        mean_deviation()
    elif type_input_stat2 == "STANDARD DEVIATION":
        standard_deviation()
    elif type_input_stat2 == "VARIANCE":
        variance()
statistics2()
#_______________________________________________________________END MAIN FUNCTION__________________________________________________________________________________________