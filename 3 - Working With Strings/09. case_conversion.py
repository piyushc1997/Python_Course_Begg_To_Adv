"""
    
Why Case Conversion is Important?

In real-world:

User may type → "PIYUSH", "piyush", "Piyush"
But you want consistent format

Used in:

Login systems
Search
Data cleaning
    
----------------------------------------------

Methods to Convert Case:

1. str.upper() - Converts to UPPERCASE
2. str.lower() - Converts to lowercase
3. str.title() - Converts to Title Case
4. str.capitalize() - Capitalizes first character

----------------------------------------------

"""

# Example 01 :- Using lower()

text = "HELLO WORLD"

print(text.lower())  # "hello world" (all characters converted to lowercase)


# Example 01.1 :- Real Example of lower() with User Input

user_input = input("Enter your email: ")  # User enters "PIYUSH"
clean_input = user_input.lower()
print(clean_input)  # "piyush@gmail.com" (all characters converted to lowercase)


# Example 02 :- Using upper()

text = "hello world"

print(text.upper())  # "HELLO WORLD" (all characters converted to uppercase)


# Example 02.1 :- Real Example of upper() with User Input

user_input = input("Enter your name: ")  # User enters "piyush"

clean_input = user_input.upper()

print(f"Hello, {clean_input}!")  # "Hello, PIYUSH!" (all characters converted to uppercase)


# Example 03 :- Using title() 

text = "hello world"

print(text.title())  # "Hello World" (each word's first character capitalized)



# Example 04 :- Using capitalize()

text = "hello world"

print(text.capitalize())  # "Hello world" (only the first character of the entire string is capitalized)



# Example 05 :- Swapping Case using swapcase()

text = "Hello World"

print(text.swapcase())  # "hELLO wORLD" (uppercase becomes lowercase and vice versa)


# Real-World Example 01 :- Normalize User Input for Consistent Storage

user_input = input("Enter your name: ")  # User enters "piyush"

normalized_input = user_input.capitalize()  # Capitalize first character

print(f"Hello, {normalized_input}!")  # "Hello, Piyush!" (first character capitalized)


# Real-World Example 02 :- Normalize Email for Case-Insensitive Comparison


email = input("Enter email: ").strip().lower()

if email.endswith("@gmail.com"):
    print("Valid Gmail") # "Valid Gmail" (email normalized to lowercase for comparison)
    

# Real-World Example 03 :- Normalize Product Names for Consistent Display

product_name = input("Enter product name: ")  # User enters "laptop"

normalized_product = product_name.title()  # Convert to title case

print(f"Product: {normalized_product}")  # "Product: Laptop" (product name displayed in title case)


# Real-World Example 04 :- Normalize Usernames for Case-Insensitive Login

username = input("Enter username: ")  # User enters "Piyush"

normalized_username = username.lower()  # Convert to lowercase for case-insensitive login

print(f"Welcome, {normalized_username}!")  # "Welcome, piyush!" (username normalized to lowercase for display)
