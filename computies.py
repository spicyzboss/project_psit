"""Computies"""
# Import module
from os import system, name
from time import sleep as delay
from src import pathway
#-----------Math subject-----------#
import src.math.complex_number as complex_num
import src.math.conic as conic
import src.math.matrix as matrix
import src.math.sequence_series as sequence
import src.math.set as mathset
import src.math.statistics1 as statistics1
import src.math.statistics2 as statistics2
import src.math.surface as surface
import src.math.volume as volume
import src.math.logic as logic
#-----------Physics subject-----------#
import src.physics.circular_motion as circular
import src.physics.current_electricity as electricity
import src.physics.horizontal_motion as horizontal
import src.physics.projectile as projectile
import src.physics.resistor as resistor
import src.physics.vertical_motion as vertical
import src.physics.work_energy as work

bootup_words = "COMPUTIES"
goodbye = "Goodluck and Goodbye :)"

def clear_screen():
    """clear screen"""
    # check os
    if name == "nt": # windows
        system("cls")
    else: # macos and linux
        system("clear")

def say_goodbye():
    """print goodbye"""
    clear_screen() # use clear screen
    print(goodbye)
    raise exit() # exit from process

def namebootup():
    """Name loading"""
    print("\t\t\x1b[5;30;47m" + bootup_words + "\x1b[0m") # "\t\t\x1b[5;30;47m" is flashing text in CLI and "\x1b[0m" is reset to default
    delay(0.5) # delay next process

def print_subject_list():
    """subject printout"""
    for subject in pathway.subjects: # Show all subjects
        print(subject)
        delay(0.5)

def subject_request_input():
    """input subject"""
    try:
        global subject
        input_word = "SELECT YOUR SUBJECTS ID : "
        subject = int(input(input_word))
    except ValueError:
        invalid_input()
        subject_selection()
    except KeyboardInterrupt:
        subject = 0
        clear_screen()

def invalid_input():
    """invalid input print"""
    clear_screen()
    print("INVALID INPUT")
    delay(0.5)

def content_request_input():
    """input content"""
    try:
        global content
        input_word = "SELECT YOUR CONTENTS ID : "
        content = int(input(input_word))
    except ValueError:
        invalid_input()
        maincontent_selection()
    except KeyboardInterrupt:
        content = 0
        clear_screen()

def subcontent_request_input():
    """input subcontent"""
    try:
        global subcontent
        input_word = "SELECT YOUR CONTENTS ID : "
        subcontent = int(input(input_word))
    except ValueError:
        invalid_input()
        subcontent_selection()
    except KeyboardInterrupt:
        subcontent = 0
        clear_screen()

def print_content_subject():
    """print subject content"""
    try:
        for content in pathway.content[subject]:
            print(content)
            delay(0.5)
    except:
        invalid_input()
        subject_selection()

def print_subcontent():
    """subcontent print function"""
    try:
        for data in pathway.content[subject][list(pathway.content[subject].keys())[content-1]]:
            print(data)
            delay(0.5)
    except:
        invalid_input()
        maincontent_selection()

def subject_checker():
    """checker function"""
    if subject:
        maincontent_selection()
    else:
        say_goodbye()

def content_checker():
    """checker function"""
    if content > 0:
        subcontent_selection()
    elif content < 0:
        invalid_input()
        maincontent_selection()
    else:
        subject_selection()

def subcontent_checker():
    """checker function"""
    if subcontent > 0:
        call_another_file()
    elif subcontent < 0:
        invalid_input()
        subcontent_selection()
    else:
        maincontent_selection()

def subcontent_selection():
    """subcontent selection"""
    clear_screen()
    namebootup()
    print_subcontent()
    subcontent_request_input()
    subcontent_checker()

def ask_to_again():
    """ask for calculate again"""
    again = input("\nTERMINATE SYSTEM?(Y/N) : ").upper()
    if again == "Y":
        say_goodbye()
    elif again == "N":
        subcontent_selection()
    else:
        invalid_input()
        subcontent_selection()

def call_another_file():
    """call file"""
    try:
        data = pathway.content[subject][list(pathway.content[subject].keys())[content-1]][list(pathway.content[subject][list(pathway.content[subject].keys())[content-1]])[subcontent-1]]
        clear_screen()
        namebootup()
        eval(data)
    except IndexError:
        invalid_input()
        subcontent_selection()
    ask_to_again()

def subject_selection():
    """main screen"""
    clear_screen()
    namebootup()
    print_subject_list()
    subject_request_input()
    subject_checker()

def maincontent_selection():
    """maincontent screen"""
    clear_screen()
    namebootup()
    print_content_subject()
    content_request_input()
    content_checker()

def start_up():
    '''Start up Computies'''
    subject_selection()

#-------------------Start project Computies-------------------#
if __name__ == "__main__":
    start_up()
