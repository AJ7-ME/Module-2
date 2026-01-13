char = input("Enter a character: ")
height = int(input("Enter the height of the triangle: "))

i = 1
while i <= height:
    spaces = height - i
    print(" " * spaces + char * i)
    i += 1