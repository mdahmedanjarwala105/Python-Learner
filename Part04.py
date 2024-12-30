# Part 4

# Exercise 1
import turtle

myScreen = turtle.Screen()

myT = turtle.Turtle()

# Drawing an equilateral triangle
myT.forward(100)
myT.right(120)
myT.forward(100)
myT.right(120)
myT.forward(100)
myT.right(120)

# New Position For Square
myT.penup()
myT.goto(-150, 0)
myT.pendown()

# Drawing a square
myT.forward(100)
myT.right(90)
myT.forward(100)
myT.right(90)
myT.forward(100)
myT.right(90)
myT.forward(100)
myT.right(90)

# New Position For Pentagon
myT.penup()
myT.goto(150, 0)
myT.pendown()

# Drawing a regular pentagon
myT.forward(100)
myT.right(72)
myT.forward(100)
myT.right(72)
myT.forward(100)
myT.right(72)
myT.forward(100)
myT.right(72)
myT.forward(100)
myT.right(72)

myT.clear()
myT.hideturtle()

# Exercise 2

import turtle

myScreen = turtle.Screen()

myT = turtle.Turtle()

# Drawing the first circle with radius 50
myT.penup()
myT.goto(0, -50)  # New Position For circle with radius 50
myT.pendown()
myT.circle(50)

# Drawing the second circle with radius 100
myT.penup()
myT.goto(0, -100)  # New Position For circle with radius 100
myT.pendown()
myT.circle(100)

# Drawing the third circle with radius 150
myT.penup()
myT.goto(0, -150)  # # New Position For circle with radius 150
myT.pendown()
myT.circle(150)

# Drawing the fourth circle with radius 200
myT.penup()
myT.goto(0, -200)  # # New Position For circle with radius 200
myT.pendown()
myT.circle(200)

myT.clear()
myT.hideturtle()

# Exercise 3

import math

factorial_of_100 = math.factorial(100)
print("\n100! =", factorial_of_100, "\n")

log_base2 = math.log2(1000000)
print("Log base 2 of 1,000,000 =", log_base2)

greatest_common_divisor = math.gcd(63, 49)
print("\nGCD of 63 and 49 =", greatest_common_divisor, "\n")

# Exercise 4

import turtle

myScreen = turtle.Screen()
myT = turtle.Turtle()

color = input("What color would you like?  ")
line_width = int(input("What line width do you want? "))
line_length = int(input("What line length do you want? "))
shape = input("Line, triangle or square? ").lower()

myT.color(color)
myT.width(line_width)

if shape == "line":
    # Drawing a line
    myT.forward(line_length)

elif shape == "triangle":
    # Drawing a triangle
    myT.forward(line_length)
    myT.right(120)
    myT.forward(line_length)
    myT.right(120)
    myT.forward(line_length)
    myT.right(120)

elif shape == "square":
    # Drawing a square
    myT.forward(line_length)
    myT.right(90)
    myT.forward(line_length)
    myT.right(90)
    myT.forward(line_length)
    myT.right(90)
    myT.forward(line_length)
    myT.right(90)

else:
    print("Invalid shape input. Please choose either line, triangle, or square.")
