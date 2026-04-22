
## Some built-in functions used with strings are :-

# 1. type() :-

name = "Piyush"
print(type(name)) # Output : <class 'str'>

# Real Use: Useful for debugging:

data = input("Enter something: ")
print(type(data))   # always str

# 2. len() :-

length_of_name = len(name)
print(length_of_name)  # 6

text = "Hello World"
print(len(text)) # 11 (including space)

# 3. str() → Convert to String

number = 123
number_str = str(number)
print(number_str)  # "123"

# 4. int() + float() with Strings

num_str = "456"

num_int = int(num_str)
print(num_int)  # 456

num_float = float(num_str)
print(num_float)  # 456.0

# 5. str() with Non-String Data

pi = 3.14159
pi_str = str(pi)
print(pi_str)  # "3.14159"

# 6. str() with Boolean Values

is_valid = True 
is_valid_str = str(is_valid)
print(is_valid_str)  # "True"

# 7. str() with None

none_value = None
none_str = str(none_value)
print(none_str)  # "None"

# 8. str() with Lists

my_list = [1, 2, 3]
list_str = str(my_list)
print(list_str)  # "[1, 2, 3]"

# 9. str() with Dictionaries

my_dict = {"name": "Piyush", "age": 30}
dict_str = str(my_dict) 
print(dict_str)  # "{'name': 'Piyush', 'age': 30}"

# 10. ord() and chr()

char = 'A'
ascii_value = ord(char)
print(ascii_value)  # 65

ascii_value = 66
char = chr(ascii_value) 
print(char)  # 'B'

## Real-World Example 01 :

name = input("Enter name: ")
age = int(input("Enter age: "))

print(f"Name: {name}")
print(f"Name length: {len(name)}")
print(f"Age after 5 years: {age + 5}")
