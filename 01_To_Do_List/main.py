from Login import send_code_to_user
from Login import save_code_to_file
from Login import generate_random_code
from Login import check_code
from List import main_list

def main():
    # Main login/signup process
    email = input("Enter your email address: ")
    password = input("Enter your password : ")
    code = generate_random_code()
    
    # Send the code to the user (you can replace this with actual email sending)
    #send_code_to_user(email, password, code)
    
    # Save the code to a file
    save_code_to_file(email, password, code)
    
    print("A verification code has been sent to your email. Please check your inbox.")

    # check code verfication
    check_code(code)

if __name__ == "__main__":
    main()