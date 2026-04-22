
## String Operators in Python :-

# 1. Concatenation (+) -> Used to join two or more strings together.

first_name = "Piyush"
last_name = "Chakraborty"

full_name = first_name + " " + last_name

print(full_name)  # "Piyush Chakraborty"
print(type(full_name))  # <class 'str'>

age = 29
age_str = str(age)

print("Age: " + age_str)  # "Age: 29"
print(type(age_str))  # <class 'str'>

# 2. Repetition (*) -> Used to repeat a string a specified number of times.

greeting = "Hello! "
repeated_greeting = greeting * 3    

print(repeated_greeting)  # "Hello! Hello! Hello!"


print("=" * 30)  # "=============================="

# 3. Membership (in) -> Used to check if a substring exists within another string.

text = "Python Developer"

print("Python" in text)   # True
print("Java" not in text) # True

email = "user@gmail.com"

print("@" in email)  # True
print(".com" in email)  # True  


# 4. Comparison Operators (==, !=, <, >, <=, >=) -> Used to compare strings based on their lexicographical order.

str1 = "apple"
str2 = "banana"

print(str1 == str2)  # False
print(str1 != str2)  # True 
print(str1 < str2)   # True (because "apple" comes before "banana" lexicographically)
print(str1 > str2)   # False    
print(str1 <= str2)  # True
print(str1 >= str2)  # False    

# Indexing ([]) -> Used to access individual characters in a string.

text = "Python"

print(text[0])  # "P"
print(text[1])  # "y"
print(text[-1]) # "n"
print(text[-2]) # "o"

# Slicing ([:]) -> Used to extract a portion of a string.

text = "Hello, World!"

print(text[0:5])  # "Hello"
print(text[7:])   # "World!"
print(text[:5])   # "Hello"
print(text[-6:])  # "World!"

# Real-World Example 01 :-

name = "Piyush"
domain = "gmail.com"

email = name + "@" + domain

print(email)           # Piyush@gmail.com
print("@" in email)    # True 
print("=" * 20)        # ====================
