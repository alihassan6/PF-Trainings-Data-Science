def sorting():
    arr = []
    while True:
        n = input("enter required length of the array: ")
        try:
            n = int(n)
        except:
            print("Invalid Input...Please use numeric digits...")
            continue
        if n < 0:
            print("Please enter a positive number. ")
            continue
        break
    for i in range(0, n):
        while True:   
            element = input("enter %d element: "%(i+1))
            try:
                element = int(element)
                arr.append(element)
            except:
                print("Invalid Input...Please use numeric digits...")
                continue
            break
    print(arr)
    arr.sort()
    print("sorted list: ", arr)
    
    print("\nDo you want to add another element in a sorted position?")
    key = input("Enter 'y' to continue or Enter any other key to exit:  ").lower()
    
    if key == "y":
        while True:
            add_element = input("enter required element: ")
            try:
                add_element = int(add_element)
                arr.append(add_element)
                arr.sort()
                print("List with number added in sorted position: ", arr)
            except:
                print("Invalid Input...Please use numeric digits...")
                continue
            break
    else:
        print("sorted list: ", arr)
    
    return

sorting()