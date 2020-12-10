"""Computies"""
# Import module
from os import system as sys
from os import name
from time import sleep as delay
import src.pathway as pathway

# Define function and variable
goodbye = "Goodluck and Goodbye :)"

def clear_screen():
    '''clear screen'''
    if name == "nt":
        sys("cls")
    else:
        sys("clear")

def namebootup(time=4):
    '''Name loading'''
    print("\t\t\x1b[5;30;47m" + 'Computies'  + "\x1b[0m") # Logo project
    delay(0.5)

def subjectlist():
    '''subject printout'''
    for subject in pathway.subject_list: # Show all subject
        print(subject)
        delay(0.5)

def request_input():
    '''input subject'''
    try:
        global subject
        subject = int(input("SELECT YOUR SUBJECT ID : "))
    except ValueError:
        clear_screen()
        print("INVALID INPUT")
        delay(1)
        mainscreen()
    except KeyboardInterrupt:
        subject = 0
        clear_screen()

def mainscreen():
    '''main screen'''
    clear_screen()
    namebootup()
    subjectlist()
    request_input()

# Main output
mainscreen()

if subject:
    clear_screen()
    namebootup(1)
    for content in pathway.subjects[subject]: # Show sub-subject
        print(' - '+content, f'({len(pathway.subjects[subject][content])})')
        delay(0.5)
    mode = list(pathway.subjects[subject].keys())[int(input('Choose number of subject: '))-0] # Find name of dict from input
    for item in pathway.subjects[subject][mode]: # Show function in sub-subject
        print('\t- '+item)
        delay(0.5)
else:
    clear_screen()
    print(goodbye)
