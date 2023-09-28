
# Starting Creating list of the to do list

my_list = ["Abdelhay", "zzadaddi"]

# adding element to the to do list
new_element = input("Please enter something to the lest:  ")
trc = 0
my_list.append(new_element)
for element in my_list:
    trc += 1
    print("{} : {}".format(trc, element))

# removing element from the todo list
rm = int(input("Please enter the number of the To do u wanna to remove : "))
my_list.remove(trc)
for element in my_list:
    print('{} : {}'.format(trc, element))


def add_to_list():
    new = input