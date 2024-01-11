# Utils
import os
import json

def key_to_continue (): # function jeo to continue
    input('[PRESS ANY KEY TO CONTINUE]')

def clean_screen(): # function to clean screen
    os.system('clear' if os.name == 'posix' else 'cls')  

def option_valide(message,start,end): # function to valide options
    while True:
        try:
            option =int(input(message))
            if option>=start and option<=end:
                return option
            else:
                print(f"Out of range({start}-{end})")
        except ValueError:
            print("please, type a valid number")