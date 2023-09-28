
# Starting Creating list of the to do list

my_list = ["Abdelhay", "zzadaddi"]




def add_to_list(my_list):
    new = input("Please enter a task : ")
    my_list.append(new)
    return my_list

def remove_list(my_list):
    rm = (int(input("Please enter the order of the number of the to do you wanna to remove : "))) - 1
    my_list.pop(rm)
    return my_list

def print_list(my_list):
    trc = 0
    for element in my_list:
        trc += 1
        print('{} : {}'.format(trc, element))


print_list(my_list)
add = add_to_list(my_list)
print_list(my_list)
rm = remove_list(my_list)
print_list(my_list)