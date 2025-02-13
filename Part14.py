# Function to print Fibonacci series up to 'n' terms
def fibonacci(n):
    first = 0  # First number in Fibonacci series
    second = 1  # Second number in Fibonacci series
    
    # If n is 1, only print the first number
    if n == 1:
        print(first)
        return
    
    # Print first two numbers
    print(first, second, end=" ")
    
    # Loop to calculate and print next numbers
    for _ in range(n - 2):  # Since first two numbers are already printed
        next_number = first + second  # Sum of last two numbers
        print(next_number, end=" ")
        first, second = second, next_number  # Update values

# Example usage
n = int(input("Enter the number of terms: "))  # Take input from user
fibonacci(n)  # Call function
