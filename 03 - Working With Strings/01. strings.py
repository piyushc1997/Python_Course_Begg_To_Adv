"""
A string (str) is used to store text data

Example:

name = "Piyush"
city = 'Kolkata'

--------------------------------------

"""

# How to Create Strings :-

# 1. Using Single Quotes

name = 'Piyush'
print(name)

# 2. Using Double Quotes

city = "Kolkata"
print(city)

# 3. Using Triple Quotes
address = '''123, ABC Street,
Kolkata - 700001'''
print(address)

# 4. Accessing Characters (Preview)

first_char = name[0]
print(first_char)
last_char = name[-1]
print(last_char)


# String Length

length_of_name = len(name)
print(length_of_name)


# Real Example 01 :-

name = "Piyush"
email = "piyush@gmail.com"

print(f"User {name} has email {email}")
