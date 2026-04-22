"""

Why Number Validation is Important?

In real-world:

User input is always string

You must check:

Is it a number?
Is it valid?

"""

# Basic Validation using isdigit() :-

age = input("Enter age: ")

if age.isdigit():
    age = int(age)
    print(age + 10)
else:
    print("Invalid input")
    
    
# Best Method (TRY-EXCEPT) :-

# Example 01 - 

try:
    num = float(input("Enter Number: "))
    print("Valid number:", num)
except:
    print("Invalid input")
    
    
# Example 02 - Validate Integer Only

try:
    num = int(input("Enter Integer: "))
    print("Valid Integer")
except:
    print("Invalid Integer")


# Example 03 - Range Validation

age = int(input("Enter age: "))

if 0 <= age <= 120:
    print("Valid age")
else:
    print("Invalid age")
    
    
# Example 04 - Combine Validation (Real Use)

try:
    age = int(input("Enter age: "))

    if age < 0:
        print("Age cannot be negative")
    else:
        print("Valid age")

except:
    print("Invalid input")
    
    
## Real-World Projects :-

# Project 1: Safe Calculator

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Sum:", a + b)

except:
    print("Invalid input")
    
    
# Project 2: Age Validator System

try:
    age = int(input("Enter age: "))

    if 18 <= age <= 60:
        print("Eligible")
    else:
        print("Not eligible")

except:
    print("Invalid input")
    
    
# Project 3: Price Validator

try:
    price = float(input("Enter price: "))

    if price > 0:
        print("Valid price")
    else:
        print("Price must be positive")

except:
    print("Invalid input")
    
    
# Project 4: Multiple Inputs Validation

try:
    marks = float(input("Enter marks: "))

    if 0 <= marks <= 100:
        print("Valid marks")
    else:
        print("Out of range")

except:
    print("Invalid input")
