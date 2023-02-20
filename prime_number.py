def prime():
    sum=0
    while True:
        try:
            n = int(input("enter number: "))
            break
        except ValueError:
            print("Invalid Input...Please enter a positive digit... ")
            continue
    if n>1:
        for i in range(2, int(n/2)+1):
            if(n%i) == 0:
                print(-1)
                break
        else:
            for i in range(0, n+1):
                sum+=i
            print("the sum of all number from 0 till the N is: ",sum)
    else:
        print(-1)
    
    return

prime()