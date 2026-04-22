"""

Everything is an object, and every object belongs to a class (data type class)
    
Example:

x = 10

Here, x is an object of the class int (integer data type) and it has properties (attributes) and behaviors (methods) associated with it.


"""

# Main Data Type Classes in Python :-

# 1. String (str) - Text data
name = "Piyush"
print(type(name))  # <class 'str'>

# 2. Integer (int) - Whole numbers
age = 25        
print(type(age))   # <class 'int'>

# 3. Float (float) - Decimal numbers
price = 99.99
print(type(price)) # <class 'float'>

# 4. Boolean (bool) - True or False
is_student = True
print(type(is_student)) # <class 'bool'>

# Complex (complex) - Complex numbers
complex_number = 2 + 3j
print(type(complex_number)) # <class 'complex'>

# Sequence Types :-

# 5. List (list) - Ordered collection of items -> can be changed after creation
fruits = ["apple", "banana", "cherry"]
print(type(fruits)) # <class 'list'>

# 6. Tuple (tuple) - Ordered, immutable collection of items -> cannot be changed after creation
coordinates = (10.0, 20.0)
print(type(coordinates)) # <class 'tuple'>

# Set Types :-

# 7. Set (set) - Unordered collection of unique items -> can be changed after creation
unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers)) # <class 'set'>

# 8. Frozen Set (frozenset) - Unordered collection of unique items -> cannot be changed after creation
immutable_numbers = frozenset({1, 2, 3, 4, 5})
print(type(immutable_numbers)) # <class 'frozenset'>

# Mapping Types :-

# 9. Dictionary (dict) - Key-value pairs -> can be changed after creation
person = {"name": "Piyush", "age": 25}  
print(type(person)) # <class 'dict'>

# 10. Range (range) - Represents an immutable sequence of numbers
number_range = range(0, 10)
print(type(number_range)) # <class 'range'>

# Binary Types (Advanced but good to know) :-

# 11. Bytes (bytes) - Immutable sequence of bytes
byte_data = b"Hello"
print(type(byte_data)) # <class 'bytes'>

# 12. Bytearray (bytearray) - Mutable sequence of bytes
mutable_byte_data = bytearray(b"Hello")
print(type(mutable_byte_data)) # <class 'bytearray'>

# 13. Memoryview (memoryview) - A memory view object is a safe way to expose the buffer protocol in Python
memory_view = memoryview(b"Hello")
print(type(memory_view)) # <class 'memoryview'>

# Some Examples :-

## len() function works with str, list, tuple, set, dict but not with int, float, bool, complex, bytes, bytearray, memoryview

text = "Hello, World!"  # str

print(len(text))    # <class 'str'>

## upper() method works with str but not with int, float, bool, complex, bytes, bytearray, memoryview

print(text.upper())  # <class 'str'> -> "HELLO, WORLD!"

## lower() method works with str but not with int, float, bool, complex, bytes, bytearray, memoryview

print(text.lower())  # <class 'str'> -> "hello, world!"

## bit_length() method works with int but not with str, float, bool, complex, bytes, bytearray, memoryview

number = 42
print(number.bit_length()) # <class 'int'> -> 6 (binary representation of 42 is 101010)


# Python Challenge 01: Variables, Data Types, Type Checking & Length

age = 25
height = 5.9
name = "Piyush"
is_student = True
future_plan = None

# Values
print("Values:")
print(age, height, name, is_student, future_plan)

# Types
print("\nTypes:")
print(type(age), type(height), type(name), type(is_student), type(future_plan))

# Lengths
print("\nLengths:")
print(len(str(age)))
print(len(str(height)))
print(len(name))
print(len(str(is_student)))
print(len(str(future_plan)))
