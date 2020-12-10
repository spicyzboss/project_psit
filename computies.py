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
    '''clear screen'''
    if name == "nt":
        sys("cls")
    else:
        sys("clear")

def say_goodbye():
    '''print goodbye'''
    clear_screen()
    print(goodbye)
    raise exit()

def namebootup():
    '''Name loading'''
    print("\t\t\x1b[5;30;47m" + bootup_words + "\x1b[0m")
    delay(0.5)

def print_subject_list():
    '''subject printout'''
    for subject in pathway.subjects: # Show all subject
        print(subject)
        delay(0.5)

def request_input(text="SUBJECTS"):
    """input subject"""
    try:
        global subject
        input_word = "SELECT YOUR %s ID : " % text
        subject = int(input(input_word))
    except ValueError:
        clear_screen()
        print("INVALID INPUT")
        delay(1)
        subject_selection()
    except KeyboardInterrupt:
        subject = 0
        clear_screen()

def print_content_subject():
    '''print subject content'''
    for content in pathway.content[subject]:
        print(content)
        delay(0.5)

def subject_selection():
    '''main screen'''
    clear_screen()
    namebootup()
    print_subject_list()
    request_input()
    checker(True)

def checker(quit=False):
    """checker function"""
    if subject:
        try:
            maincontent_selection()
            if not subject:
                subject_selection()
        except KeyError:
            subject_selection()
    elif quit:
        say_goodbye()
    else:
        maincontent_selection()

def maincontent_selection():
    '''maincontent screen'''
    clear_screen()
    namebootup()
    print_content_subject()
    request_input("CONTENTS")
    checker()

while True:
    subject_selection() # Main output
