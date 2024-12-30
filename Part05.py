# Part 5


# Exercise 1

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    if month[0] == 'J':
        print(month)
        
print("\n")

# Exercise 2

for num in range(100):
    if num % 2 == 0 and num % 5 == 0:
        print(num)

print("\n")

# Exercise 3

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for char in horton:
    if char in vowels:
        print(char)
