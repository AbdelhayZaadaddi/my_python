
# Starting Creating list of the to do list

my_list = ["Abdelhay", "zzadaddi"]

# adding element to the to do list
new_element = input("Please enter something to the lest:  ")
trc = 0
my_list.append(new_element)
for element in my_list:
    trc += 1
    print("{} : {}".format(trc, element))

trc = 0
# removing element from the todo list
rm = (int(input("Please enter the number of the To do u wanna to remove : ")) - 1)
my_list.pop(rm)
for element in my_list:
    trc += 1
    print('{} : {}'.format(trc, element))


def add_to_list(my_list, new):
    new = input("Please enter a task : ")
    my_list.append(new)
    return my_list

def remove_list(my_list, rm):
    rm (int(input("Please enter the order of the number of the to do you wanna to remove")))