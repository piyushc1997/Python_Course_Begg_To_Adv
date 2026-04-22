""" 
print() is a built-in function used to display output on the screen.

Basic Example:

print("Hello World")

Output:
Hello World

-----------------------------------------------

Why print() is Important?

To see output
To debug code
To show results to users

"""

# (A) Printing Text (String)

print("Hello World!")  # Output: Hello World!

# (B) Printing Numbers

print(42)  # Output: 42
print(3.14)  # Output: 3.14

# (C) Printing Variables

name = "Piyush"
age = 25

print(name)  # Output: Piyush
print(age)   # Output: 25

# (D) Printing Multiple Items

name = "Piyush"
age = 25

print(name, age)  # Output: Piyush 25

# Understanding sep (Separator)

print(name, age, sep=" - ")  # Output: Piyush - 25

print("2026", "04", "13", sep="/")  # Output: 2026/04/13

# Understanding end (End Character)

print("Hello", end=" ")
print("World")  # Output: Hello World

print("Loading", end="...")  # Output: Loading...

# Printing with Formatting (Important)

# (A) Using f-strings (Best Method)

name = "Piyush"
age = 25

print(f"My name is {name} and I am {age} years old") # Output: My name is Piyush and I am 25 years old

# (B) Using str.format()

name = "Piyush"
age = 25
print("My name is {} and I am {} years old".format(name, age)) # Output: My name is Piyush and I am 25 years old

# Real-World Mini Example :-

name = "Piyush"
salary = 50000
bonus = 5000

total = salary + bonus

print(f"Employee: {name}")    
print(f"Total Salary: {total}") 

# Debugging Example :-

x = 10
y = 5

print("x value:", x)
print("y value:", y)

print("Sum:", x + y) 
