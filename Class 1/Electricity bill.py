units = int(input("Enter the number of units consumed: "))
if units < 0:
    print("Invalid input. Please enter a non-negative number.")
if (units < 50):
    amount = units * 2.6
    surcharge = 25
elif (units >= 50 and units < 100):
    amount = 130 + ((units -50) * 3.25)
    surcharge = 35
elif (units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

tb = amount + surcharge
print("\nThe electricity bill is:", tb)




















































































































