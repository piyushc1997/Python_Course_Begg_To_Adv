"""
A variable is used to store data (values) in a program.

A variable is like a container (box) that holds some value.

------------------------------------------------------------
Example:

salary = 50000

Here:
salary → variable name
50000 → value stored

------------------------------------------------------------

Why Do We Need Variables?
 To store data
 To manipulate data
 To make code reusable

------------------------------------------------------------

Rules for Naming Variables (Important)

1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
2. Variable names cannot start with a number.
3. Variable names can only contain letters, numbers, and underscores.
4. Variable names are case-sensitive (age and Age are different).
5. Variable names cannot be a reserved keyword (like if, for, while, etc.).
6. Variable names should be descriptive (like age, name, salary, etc.) for better readability.
7. Variable names should not contain spaces. Use underscores (_) instead (like first_name, last_name).
8. Variable names should not be too long or too short. Aim for a balance (like user_age, not u or userage).
9. Variable names should not use special characters (like @, #, $, etc.).
10. Variable names should not be the same as built-in function names (like print, input, etc.).
11. Variable names should not be the same as data types (like int, str, list, etc.).
12. Variable names should not be the same as module names (like math, os, etc.).
13. Variable names should not be the same as class names (like Person, Car, etc.).
14. Variable names should not be the same as constants (like PI, GRAVITY, etc.).
15. Variable names should not be the same as boolean values (like True, False).
16. Variable names should not be the same as None.
17. Variable names should not be the same as special variables (like __name__, __file
__, etc.).
18. Variable names should not be the same as keywords (like if, else, for, while, etc.).
19. Variable names should not be the same as operators (like +, -, *, /, etc.).
20. Variable names should not be the same as punctuation (like ., ,, ;, :, etc.).
21. Variable names should not be the same as whitespace (like space, tab, newline,  etc.).
22. Variable names should not be the same as comments (like #, //, /*, */, etc.).
23. Variable names should not be the same as docstrings (like """ """, ''' ''   ', etc.).
24. Variable names should not be the same as escape characters (like \n, \t , \\, \', \", etc.).
25. Variable names should not be the same as literals (like "Hello", 42,    3.14, True, False, None, etc.).
26. Variable names should not be the same as functions (like print, input, len, etc.).      

 Some Examples - Allowed: 
 
name = "Piyush"
age1 = 25
_user = "admin"

Some Examples - Not Allowed:

1name = "Piyush"  # Not allowed (starts with a number)
user-name = "admin"  # Not allowed (contains a hyphen)
user name = "admin"  # Not allowed (contains a space)
print = "Hello"  # Not allowed (same as built-in function name)
int = 42  # Not allowed (same as data type name)

"""

# Types of Data Stored in Variables :-

# (A) String(text)

name = "Piyush"
print(name)  # Output: Piyush

# (B) Integer (whole number)

age = 25
print(age)  # Output: 25

# (C) Float (decimal number)

height = 5.9
print(height)  # Output: 5.9

# (D) Boolean (True or False)

is_student = True
print(is_student)  # Output: True

is_graduate = False
print(is_graduate)  # Output: False 

# (E) None (represents no value)

result = None
print(result)  # Output: None

# Changing Variable Value 

name = "Piyush"
print(name)  # Output: Piyush
name = "Rahul"
print(name)  # Output: Rahul (value is changed to Rahul)

# Multiple Assignment 

x, y, z = 10, 20, 30
print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30

x = y = z = 100
print(x)  # Output: 100
print(y)  # Output: 100
print(z)  # Output: 100

# Type Checking (Very Useful)

name = "Piyush"
age = 25
print(type(name))  # Output: <class 'str'> (string)
print(type(age))   # Output: <class 'int'> (integer)

# Variable Naming Conventions (Important)

# (A) snake_case (Most Common in Python)
first_name = "Piyush"
last_name = "Sharma"

# (B) camelCase
firstName = "Piyush"
lastName = "Sharma"

# (C) PascalCase
FirstName = "Piyush"
LastName = "Sharma"

# Type Casting (Conversion) :

age = 25
age_str = str(age)  # Convert integer to string
print(age_str)  # Output: "25"
print(type(age_str))  # Output: <class 'str'>

height = 5.9
height_int = int(height)  # Convert float to integer (truncates decimal part)
print(height_int)  # Output: 5
print(type(height_int))  # Output: <class 'int'>

# Note: Type casting can lead to data loss (like converting float to int) and should be done carefully.

# Real-World Example :

name = "Piyush"
age = 25
print(f"My name is {name} and I am {age} years old")  # Output: My name is Piyush and I am 25 years old


name = "Piyush"
salary = 50000
bonus = 5000

total_salary = salary + bonus

print(f"Employee: {name}")
print(f"Total Salary: {total_salary}")


# Challange 01 :-

domain = "datawithbaraa.com"

print(f"info@{domain}")
print(f"support@{domain}")
print(f"www.{domain}")
