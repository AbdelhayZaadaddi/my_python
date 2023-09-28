# Starting Creating list of the to-do list

star = 1  # Moved star here

def add_to_list(my_list):
    new = input("Please enter a task : ")
    my_list.append(new)
    return my_list

def remove_list(my_list):
    rm = (int(input("Please enter the order of the number of the to-do you want to remove : "))) - 1
    my_list.pop(rm)
    return my_list

def print_list(my_list):
    trc = 0
    for element in my_list:
        trc += 1
        print('{} : {}'.format(trc, element))

def main_list():
    global star  # Declare 'star' as a global variable
    my_list = []  # Initialize my_list here
    while star != 0:
        star = int(input("Please enter '1' to start and '0' to exit: "))
        if star == 1:
            print_list(my_list)
            my_list = add_to_list(my_list)
            print_list(my_list)
            my_list = remove_list(my_list)
            print_list(my_list)