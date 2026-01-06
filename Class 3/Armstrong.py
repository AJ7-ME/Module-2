while True: 
    number = int(input("Enter a number: "))
    num = number
    numb = number
    sum1 = 0
    temp1 = number
    while temp1 > 0:
        digit1 = temp1 % 10
        sum1 += digit1 ** 3
        temp1 //= 10
    sum2 = 0
    temp2 = number
    while temp2 > 0:
        digit2 = temp2 % 10
        sum2 += digit2 ** 4
        temp2 //= 10
    sum3 = 0
    temp3 = number
    while temp3 > 0:
        digit3 = temp3 % 10
        sum3 += digit3 ** 5
        temp3 //= 10
    if number == sum1 or num == sum2 or numb == sum3:
        print(number, "is an Armstrong number\n")
    else:
        print(number,"is not an Armstrong number\n")