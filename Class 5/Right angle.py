while True:

    print("Right angled pattern of ^")
    n =  int(input("Enter the number of rows:\n"))
    for i in range(n):
        for j in range(i+1):
            print("^", end="")
        print()