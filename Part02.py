# Part 2

# Exercise Question 1

grades = ['A', 'C', 'E', 'B', 'D', 'F', 'A', 'C', 'E', 'B', 'D', 'F', 'A', 'C', 'A', 'D', 'C', 'A', 'E', 'D']

frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('E'), grades.count('F')]

print(frequency, "\n")

# Exercise Question 2

dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

print(dog_breeds)

herding_dogs = dog_breeds[:2]

print(herding_dogs)

tiny_dogs = [dog_breeds[-1]]

print(tiny_dogs)

persian_in_dog_breeds = 'Persian' in dog_breeds

print(persian_in_dog_breeds, "\n")

# Exercise Question 3

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

name_list = [first_name, last_name]

initials = first_name[0] + last_name[0]

average_length = (len(first_name) + len(last_name)) / 2

print("List:", name_list)
print("Initials:",initials)
print("Average length:", average_length)
