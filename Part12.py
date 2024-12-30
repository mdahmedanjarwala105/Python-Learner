# Part 12

# Problem 1

def safeOpen(filename):
    """
    Attempts to open the file with the given filename for reading.
    Returns the file object if successful, or None if the file does not exist.
    """
    try:
        # Attempt to open the file
        file = open(filename, 'r')
        return file
    except FileNotFoundError:
        # If file not found, return None
        return None


inputFile = safeOpen('ghost.txt')
print(inputFile)


f = open('example.txt', 'w')
f.write('This is a test file.')
f.close()


inputFile = safeOpen('example.txt')
if inputFile:
    print(inputFile.read())
    inputFile.close()

# Problem 2

def safeFloat(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        # If an exception occurs, return 0.0
        return 0.0

# Example usage
print(safeFloat('123.45'))
print(safeFloat('abc'))
print(safeFloat('123'))
print(safeFloat(567))
print(safeFloat(None))

# Problem 3

def safeFloat(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return 0.0

def safeOpen():
    attempts = 0
    while attempts < 2:
        try:
            filename = input("Enter file name: ")
            return open(filename, 'r')
        except FileNotFoundError:
            attempts += 1
            if attempts < 2:
                print("File not found. Please try again.")
            else:
                print("File not found. Yet another human error. Goodbye.")
                return None

def averageSpeed():
    file = safeOpen()
    if not file:
        return

    total_speed = 0
    count = 0

    for line in file:
        readings = line.split()
        for reading in readings:
            speed = safeFloat(reading)
            if speed > 2:
                total_speed += speed
                count += 1

    file.close()

    if count > 0:
        average = total_speed / count
        print("Average speed is", round(average, 2), "miles per hour.")
    else:
        print("No valid readings to calculate an average.")

# Example
averageSpeed()
