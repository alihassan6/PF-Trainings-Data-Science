def problem1_2_3_using_tuple():
    print("\t\tEnter 'exit' to exit the program.")
    print("""this function solves first three problems.\nit takes input in form of tuple.
    when 11th value will be added, first indexed value will be popped out.\nat the end it will print list till nth index.""")
    my_list = []
    while True:
        key = input("Enter a key: ").lower()
        if key == "exit":
            break
        value = input("Enter a value: ")

        key_exists = False
        for pair in my_list:
            if pair[0] == key:
                key_exists = True
                print("Error: Key already exists. Please enter a different key.")
                break
    
        if not key_exists:
            my_list.append((key, value))
        
        if len(my_list) > 10:
            my_list.pop(0)    

    print("List of tuples:", my_list)

    n = int(input("Enter nth index till where you want to print list: "))
    if not 0 <= n <= 10:
        print("Invalid input.")
    else:
        print(my_list[:n])
    return
#
###################################################
#
def problem1_using_lists():
    value_list = []
    key_list = []

    while len(value_list)<10:
        key = input("Enter key:  ")
        if key in key_list:
            print("key already exists. Enter another key.")
            continue
        else:
            key_list.append(key)
            value = input("Enter value:  ")
            value_list.append(value)

    print(value_list)
    return
#
####################################################
#
def problem1_using_dictionary():
    my_dict = {}

    while len(my_dict) < 10:
        key = input("Enter key: ")
        if key in my_dict:
            print("key already exists. Enter another key.")
        else:
            value = input("Enter value: ")
            my_dict[key] = value

    value_list = list(my_dict.values())
    print("Resultant list of values:", value_list)
    return
#
####################################################
#
def problem2():
    def add_to_list(list_2, element):
        if len(list_2) < 5:
            list_2.append(element)
        else:
            list_2.pop(0)
            list_2.append(element)
    #        list_2.insert(0, element)

    list_2 = []
    print("\t\t\tEnter 'exit' to exit program")
    while True:
        element = input("Enter value:  ").lower()
        if element == "exit":
            break
    
        add_to_list(list_2, element)
        print(list_2)
    return
#
#####################################################
#
def problem3():
    random_list = [8,6,4,1,9]

    value = int(input("Enter value:  "))
    if value in random_list:
        print("value already present in the list")
    else:
        random_list.append(value)
        print(random_list)
    return
#
######################################################
#
def problem4_with_0():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        array.append(row)

    for i in range(rows):
        for j in range(cols):
            print(array[i][j], end=" ")
        print()
    return
#
######################################################
#
def problem4_using_random():
    import random
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 9))
        array.append(row)

    for i in range(rows):
        for j in range(cols):
            print(array[i][j], end=" ")
        print()
    return
#
######################################################
#
