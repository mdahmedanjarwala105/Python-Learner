# Part 1

# Exercise B
months_in_year = 12
days_in_weak = 7
days_in_month = 30

print(months_in_year)
print(days_in_weak)
print(days_in_month)

# Exercise C
distance_in_kilometers = 21.73
weight_in_kilograms = 28.34
temperature_in_celcius = 24.2

print(distance_in_kilometers)
print(weight_in_kilograms)
print(temperature_in_celcius)

#Exercise D
famous_quote = "New York the city which never sleeps."
name_of_person = "Mohammed Ahmed Anjarwala"
favourite_city = "Los Angelas"

print(famous_quote)
print(name_of_person)
print(favourite_city)

# TextBook Exercise 1.1

# Question 1

# print("hello world"
print("If you leave out one of the parantheses it gives an error -> SyntaxError: '(' was never closed")

# print "hello world"
print("If we leave out the parantheses marks it gives an error -> SyntaxError: Missing parentheses in call to 'print'.")

#Question 2

# print("hello world)
print("If we leave out one of the quotation it gives an error -> SyntaxError: unterminated string literal")

# print(hello world)
print("If we leave out the quotation it gives an error -> SyntaxError: invalid syntax.")

# Question 3

a = 2++2
print(a)

# Question 4


"""
notation_Leading_Zero = 011
print(notation_Leading_Zero)
"""

print("The notation leading zero if its 011 then it gives an error -> SyntaxError: leading zeros in decimal integer literals are not permitted")


# Question 5

"""
values_With_No_Operator = 6 12
print(values_With_No_Operator)
"""

print("If there are two values with no operation between them then it gives an error -> SyntaxError: invalid syntax")

# Textbook Exercise 1.2

# Question 1

minutes = 42
seconds = 42

total_Seconds = (minutes * 60) + seconds
print (total_Seconds)

# Question 2

kilometers = 10
miles_Per_kilometer = 1.61

total_Miles = kilometers/miles_Per_kilometer

#Question 3

time_In_Minutes = 42
time_In_Seconds = 42
distance_In_Km = 10

total_Time_In_Minutes = time_In_Minutes + time_In_Seconds / 60

km_To_Miles = 0.621371
distance_In_Miles = distance_In_Km * km_To_Miles

average_pace_minutes_per_mile = total_Time_In_Minutes / distance_In_Miles

pace_In_Minutes = int(average_pace_minutes_per_mile)
pace_In_Seconds = int((average_pace_minutes_per_mile - pace_In_Minutes) * 60)

average_Speed_In_mph = distance_In_Miles / (total_Time_In_Minutes / 60)

print("Average Pace:", pace_In_Minutes, "minutes", pace_In_Seconds, "seconds per mile")
print("Average Speed:", average_Speed_In_mph, "miles per hour")

# Textbook Exercies 2.1

# Question 1
# 42 = n
print("42 = n, it gives an error -> SyntaxError: cannot assign to literal")

# Question 2
x = y = 1

print(x)
print(y)

# Question 3
semicolon_In_Statement = "Putting a semicolon at the end of python statement";
print(semicolon_In_Statement)

# Question 4
# period_In_Statement = "Putting a period at the end of statement".
print("If we put a period at the end of statement it gives an error -> SyntaxError: invalid syntax")

# Question 5
"""
x = 10
y = 20
z = xy
"""

print("If we try multiplying x and y like this: xy it gives an error -> NameError: name 'xy' is not defined.")

# Textbook Exercise 2.2

# Question 1
radius_Of_Sphere = 5
value_Of_Pie = 3.14
volume_Of_Sphere = (4/3) * value_Of_Pie * (radius_Of_Sphere ** 3)

print(volume_Of_Sphere)

# Question 2

cover_Price = 24.95
discount = 40/100
number_Of_Copies = 60
shipping_Cost_Of_First_Copy = 3.00
shipping_Cost_Of_Additional_Copy = 0.75

discount_Price = cover_Price * (1 - discount)

total_Cost_Of_Books = discount_Price * number_Of_Copies

total_Shipping_Cost = shipping_Cost_Of_First_Copy + (number_Of_Copies - 1) * shipping_Cost_Of_Additional_Copy

total_Wholesale_Cost = total_Cost_Of_Books + total_Shipping_Cost

print("The total wholesale cost for", number_Of_Copies, "copies is $", total_Wholesale_Cost)

# Question 3

starting_Hours = 6
starting_Minutes = 52

easy_Pace_Per_Mile = 8 + 15 / 60
tempo_Pace_Per_Mile = 7 + 12 / 60

total_Easy_Pace_Time = 2 * easy_Pace_Per_Mile
total_Tempo_Pace_Time = 3 * tempo_Pace_Per_Mile
total_Running_Time = total_Easy_Pace_Time + total_Tempo_Pace_Time

start_Time_In_Minutes = starting_Hours * 60 + starting_Minutes

new_Time_In_Minutes = start_Time_In_Minutes + total_Running_Time

final_Hours = int(new_Time_In_Minutes // 60)
final_Minutes = int(new_Time_In_Minutes % 60)

final_Hours = final_Hours % 12 or 12

print("You will get home at", final_Hours, final_Minutes, "AM")
