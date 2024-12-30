# Part 11

# Problem 1

class Dog:
    """A class to represent a dog with a name and breed."""

    def __init__(self, name, breed):
        """Initialize a Dog object with a name and breed."""
        self.name = name
        self.breed = breed

# Testing the class
sugar = Dog('Sugar', 'border collie')
print(sugar.name)
print(sugar.breed)

# Problem 2

class Dog:
    """A class to represent a dog with a name, breed, and a list of tricks."""

    def __init__(self, name, breed):
        """Initialize a Dog object with a name, breed, and an empty list of tricks."""
        self.name = name
        self.breed = breed
        self.tricks = []

# Testing the class
sugar = Dog('Sugar', 'border collie')
print(sugar.name)
print(sugar.breed)
print(sugar.tricks)

# Problem 3

class Dog:
    """A class to represent a dog with a name, breed, and a list of tricks."""

    def __init__(self, name, breed):
        """Initialize a Dog object with a name, breed, and an empty list of tricks."""
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        """Add a trick to the dog's list of tricks and print a message."""
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

# Test the class
sugar = Dog('Sugar', 'border collie')
sugar.teach('frisbee')
print(sugar.tricks)

# Problem 4

class Dog:
    """A class to represent a dog with a name, breed, and a list of tricks."""

    def __init__(self, name, breed):
        """Initialize a Dog object with a name, breed, and an empty list of tricks."""
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        """Add a trick to the dog's list of tricks and print a message."""
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

    def knows(self, trick):
        """Check if the dog knows the specified trick."""
        if trick in self.tricks:
            print(f"Yes, {self.name} knows {trick}")
            return True
        else:
            print(f"No, {self.name} doesn't know {trick}")
            return False

# Testing the class
sugar = Dog('Sugar', 'border collie')
sugar.teach('frisbee')
print(sugar.knows('frisbee'))
print(sugar.knows('arithmetic'))

# Problem 5

class Dog:
    """A class to represent a dog with a name, breed, and a list of tricks."""
    
    species = 'Canis familiaris'

    def __init__(self, name, breed):
        """Initialize a Dog object with a name, breed, and an empty list of tricks."""
        self.name = name
        self.breed = breed
        self.tricks = []

    def teach(self, trick):
        """Add a trick to the dog's list of tricks and print a message."""
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

    def knows(self, trick):
        """Check if the dog knows the specified trick."""
        if trick in self.tricks:
            print(f"Yes, {self.name} knows {trick}")
            return True
        else:
            print(f"No, {self.name} doesn't know {trick}")
            return False

# Testing the class
print(Dog.species)
sugar = Dog('Sugar', 'border collie')
print(sugar.species)
