import turtle
x = int(input("How many sides?\n"))
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500,700)
polygon = turtle.Turtle() 
num_sides = (x)
side_lenght = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_lenght)
    polygon.right(angle)
turtle.done()