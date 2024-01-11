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

def load_json(file): # Funtion to load Json
  try:

    # Try to open the file json to conver it to list
    with open(os.path.join("data", f"{file}.json"), 'r') as json_file: 
      file_list = json.load(json_file)
    return file_list
  
  except Exception as e:
    return None

def key_to_continue (): # Function press any to continue
   input('[PRESS ANY KEY TO CONTINUE]')

def code_generator(prefix, start, end):
    return [f"{prefix}{i}" for i in range(start, end + 1)]

def save_json(list, filejson): # Funcion para guardar la informacion en JSON
    try:
      
      with open(os.path.join("data", f"{filejson}.json"), 'w') as archivo_json: # Open Json as format write
        json.dump(list, archivo_json, indent = 4) # Modify Json indentaded 4 lines

    except FileNotFoundError: # Print a message if the file doesn't exist
        print("The file doesn't exist. There may not be any campers saved yet.")

    except json.JSONDecodeError: # Print another message if  the format is incorrect
        print("Error to decodify the file. Format could be incorrect.")

    except Exception as e: # print another message if something make an error unknowed
        print(f"Error Unknowed:{e}")