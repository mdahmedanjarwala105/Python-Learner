# Part 3

# Exercise Question 1

a = 3
b = 4
c = 5

if a < b:
    print("OK")

if c < b:
    print("OK")

if a + b == c:
    print("OK")

if a**2 + b**2 == c**2:
    print("OK \n")

# Exercise Question 2

a = 3
b = 4
c = 5

if a < b:
    print("OK")
else:
    print("Not OK")

if c < b:
    print("OK")
else:
    print("Not OK")

if a + b == c:
    print("OK")
else:
    print("Not OK")

if a**2 + b**2 == c**2:
    print("OK \n")
else:
    print("Not OK \n")

# Exercise Question 3

print("Enter the lengths of three sticks")
first_stick = float(input("Length of the first stick: "))
second_stick = float(input("Length of the second stick: "))
third_stick = float(input("Length of the third stick: "))

if first_stick + second_stick > third_stick and first_stick + third_stick > second_stick and second_stick + third_stick > first_stick:
    print("The sticks can form a triangle.")
elif first_stick + second_stick == third_stick or first_stick + third_stick == second_stick or second_stick + third_stick == first_stick:
    print("The sticks form a degenerate triangle.")
else:
    print("The sticks cannot form a triangle.")
