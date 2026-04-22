"""
Data types define what kind of data a variable holds

Example:

name = "Piyush"   # String
age = 25          # Integer
price = 99.99     # Float

Python automatically detects type (dynamic typing)

------------------------------------------

Why Data Types are Important?

Because:

 Different data → different operations
 Prevents errors
 Helps in logic building

------------------------------------------

"""

# Main Data Types in Python :-

# 1. String (str) - Text data
name = "Piyush"         

# 2. Integer (int) - Whole numbers
age = 25

# 3. Float (float) - Decimal numbers
price = 99.99

# 4. Boolean (bool) - True or False
is_student = True
is_student = False

# 5. List (list) - Ordered collection of items -> can be changed after creation
fruits = ["apple", "banana", "cherry"]

# 6. Tuple (tuple) - Ordered, immutable collection of items -> cannot be changed after creation
coordinates = (10.0, 20.0)

# 7. Dictionary (dict) - Key-value pairs -> can be changed after creation
person = {"name": "Piyush", "age": 25}  

# 8. Set (set) - Unordered collection of unique items -> can be changed after creation
unique_numbers = {1, 2, 3, 4, 5}

# Type Checking :-

print(type(name))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(price))         # <class 'float'>
print(type(is_student))    # <class 'bool'>
print(type(fruits))        # <class 'list'>
print(type(coordinates))   # <class 'tuple'>
print(type(person))        # <class 'dict'>
print(type(unique_numbers)) # <class 'set'>


# Type Conversion (Very Important) :-

# Convert integer to float
age_float = float(age)    # 25.0

# Convert float to integer
price_int = int(price)   # 99

# Convert integer to string
age_str = str(age)      # "25"

# Convert string to integer (if possible)
age_from_str = int(age_str)  # 25

# Convert string to float (if possible)
price_from_str = float(str(price))  # 99.0

# Convert list to tuple
fruits_tuple = tuple(fruits)  # ("apple", "banana", "cherry)

# Convert tuple to list
coordinates_list = list(coordinates)  # [10.0, 20.0]

# Convert dictionary keys to a list
person_keys = list(person.keys())  # ["name", "age"]

# Convert dictionary values to a list
person_values = list(person.values())  # ["Piyush", 25]

# Convert set to list
unique_numbers_list = list(unique_numbers)  # [1, 2, 3, 4, 5]

# Convert list to set
unique_numbers_set = set(unique_numbers_list)  # {1, 2, 3, 4, 5}

# Note: Not all conversions are possible (e.g., converting "hello" to int will raise an error)
