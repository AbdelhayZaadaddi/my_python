import random
import string

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


# Main login/signup process
email = input("Enter your email address: ")
password = input("Enter your password : ")
code = generate_random_code()
    
    # Send the code to the user (you can replace this with actual email sending)
send_code_to_user(email, password, code)
    
    # Save the code to a file
save_code_to_file(email, password, code)
    
print("A verification code has been sent to your email. Please check your inbox.")