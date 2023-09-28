import random
import string
from List import main_list

# Function to generate a random code
def generate_random_code(length = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to send the code to the user 
def send_code_to_user(email, password, code):
    print('Email : {}\nPassword : {}\nCode : {}'.format(email, password, code))

# Function to save the code in a file
def save_code_to_file(email, password, code):
    with open("Verfication_codes.text", "a") as file:
        file.write('Email : {}\nPassword : {}\nCode : {}'.format(email, password, code))


def check_code(code):
    new_code = input("Please enter the Vercation code : ")
    if new_code == code:
        main_list()
    else:
        print("Fuck you man!")
        exit()