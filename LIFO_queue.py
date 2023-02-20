def LIFO_queue():
    i=1
    LIFO_queue = []
    print("Empty.\n First add elements to the LIFO_queue")
    while True:
        print("\nEnter 'e' to stop adding and print")
        add = input("Add %d element to the LIFO_queue:  "%i)
        i+=1
        LIFO_queue.append(add)
        print("\nAdded")
        if (add == "e" or add == "E"):
            LIFO_queue.pop()
            print(LIFO_queue)
            break
    
    while True:
        print("\nYou want to add another element to LIFO_queue or pop an element out? ")
        option = input("Enter 'a' to add\nEnter 'p' to pop out\nEnter 'e' to exit\n ").lower()
    
        if option == "e":
            print("EXIT")
            break
        if option == "a":
            new = input("\nenter number to add: ")
            LIFO_queue.append(new)
            print("added: ", LIFO_queue)
        if option == "p":
            if len(LIFO_queue) == 0:
                print("Empty... You can't pop out")
                continue
            else:
                LIFO_queue.pop()
                print("remaining: ", LIFO_queue)
        if (option!="a" and option!="p" and option!="e"):
            print("\nInvalid Input.\nPlease Enter Valid Option.")
        
    return

LIFO_queue()