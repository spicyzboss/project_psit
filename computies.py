"""Computies"""
# Import module
from os import system as sys
from os import name
from time import sleep as delay
import src.pathway as pathway

# Define function and variable
bootup_words = "COMPUTIES"
goodbye = "Goodluck and Goodbye :)"

def clear_screen():
    """clear screen"""
    if name == "nt":
        sys("cls")
    else:
        sys("clear")

def say_goodbye():
    """print goodbye"""
    clear_screen()
    print(goodbye)
    raise exit()

def namebootup():
    """Name loading"""
    print("\t\t\x1b[5;30;47m" + bootup_words + "\x1b[0m")
    delay(0.5)

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
    delay(1)

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

def print_content_subject():
    """print subject content"""
    try:
        for content in pathway.content[subject]:
            print(content)
            delay(0.5)
    except KeyError:
        invalid_input()
        subject_selection()

def subject_checker():
    """checker function"""
    if subject:
        maincontent_selection()
    else:
        say_goodbye()

def content_checker():
    """checker function"""
    if content > 0:
        call_another_file()
    elif content < 0:
        invalid_input()
        maincontent_selection()
    else:
        subject_selection()

def call_another_file():
    """call file"""
    namebootup()
    for data in list(pathway.content[subject].keys())[content-1]:
        eval(data)

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

while True:
    subject_selection() # Main output