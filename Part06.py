# Part 6

# Exercise 1: a
def hasFinalLetter(strList, letters):
    """Return a list of strings from strList that end with any letter in letters."""
    result = []
    
    for string in strList:
        if string[-1] in letters:
            result.append(string)

    return result

strList = ["green", "red", "blue",]
letters = "dE"
result = hasFinalLetter(strList, letters)
print(result)

# Exercise 1: b
# Test Case 1:
strList1 = ["apple", "banana", "cherry"]
letters1 = "ae"
result1 = hasFinalLetter(strList1, letters1)
print(result1)

# Test Case 2: No strings ending with letters in the given string
strList2 = ["hello", "world", "python"]
letters2 = "xyz"
result2 = hasFinalLetter(strList2, letters2)
print(result2)

# Test Case 3: Mixed case letters in the given string
strList3 = ["Apple", "Banana", "Cherry"]
letters3 = "Ae"
result3 = hasFinalLetter(strList3, letters3)
print(result3)

# Exercise 2: a
def isDivisible(maxInt, tupleints):
    """
    returns True if the first integer is divisible by the second integer.
    """
    divisible_numbers = []

    for num in range(1, maxInt):
        if num % tupleints[0] == 0 and num % tupleints[1] == 0:
            divisible_numbers.append(num)
    
    return divisible_numbers


maxInt = 20
tuple_ints = (2, 5)

result = isDivisible(maxInt, tuple_ints)
print("Divisible numbers:", result)

# Exercise 2: b
# Test Case 1: Normal Case
maxInt_1 = 30
tuple_ints_1 = (3, 5)
result_1 = isDivisible(maxInt_1, tuple_ints_1)
print("Test Case 1 Result:", result_1)  # Expected output: [15]

# Test Case 2: Empty List Result
maxInt_2 = 10
tuple_ints_2 = (7, 9)
result_2 = isDivisible(maxInt_2, tuple_ints_2)
print("Test Case 2 Result:", result_2)

# Test Case 3: Mixed Values
maxInt_3 = 50
tuple_ints_3 = (2, 10)
result_3 = isDivisible(maxInt_3, tuple_ints_3)
print("Test Case 3 Result:", result_3)
