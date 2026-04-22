"""

What is Boolean?

Boolean is a data type that has only 2 values: True and False


"""

# Simple Example :-

is_active = True
is_logged_in = False

print(is_active)
print(is_logged_in)


# Small Practice :-

print(5 > 3)      # True
print(10 == 5)    # False
print(bool(""))   # False
print(bool("Hi")) # True


# Example 01 :-

email = "cpiyush563@gmail.com"
phone = "0176-123456"
username = "piyuc1997"

# Allows registration
# if any field is filled

print (any([email, phone, username]))


# Example 01.1 :-

# Allows registration
# Only of all fields is filled

print (all([email, phone, username]))


# Example 02 :- Uisng -> isinstace()

print(isinstance(123, int))

print("Hello" .endswith("o"))

print("Hello" .startswith("o"))
