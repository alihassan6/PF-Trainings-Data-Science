def students():
    total = 0
    math = 0
    bio = 0
    
    while total <= 0:
        try:
            total = int(input("total students: "))
            if total <= 0:
                print("The total number of students must be a positive integer.")
        except ValueError:
            print("Please input integer only...")  
            continue
            
    while True:
        try:
            math = int(input("math students:"))
            
            if (math > total):
                print("invalid... sum of math and bio students cannot be greater than total")
            else:   
                break
        except ValueError:
            print("Please input integer only...") 
            
    
    while True:
        try:
            bio = int(input("bio students:"))
            
            if (math + bio > total):
                print("invalid... sum of math and bio students cannot be greater than total")
            else:
                break
        except ValueError:
            print("Please input integer only...")  
            continue
    
    
    
    
    without_math = total - math
    print("Students without math :", without_math)
    without_bio = total - bio
    print("Students without bio: ", without_bio)
    with_math_bio = math + bio
    print("with math and bio: ", with_math_bio)
    return

students()