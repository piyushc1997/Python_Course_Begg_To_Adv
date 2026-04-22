"""
    
Validation means:

Checking if a string meets certain conditions

In real-world:

Username should be letters only
Phone number should be digits
Password rules
    
"""

# Example 01 :- isalpha() → Only Letters

text = "Piyush"

print(text.isalpha()) # Output : True


# Example 02:- isdigit() → Only Digits

text = "12345"

print(text.isdigit()) # Output : True



# Example 03 :- isalnum() → Letters + Numbers

text = "Piyush123"

print(text.isalnum()) # Output : True


# Example 05 :- isspace() → Only Whitespace

text = "    "

print(text.isspace()) # Output : True


# Example 06 :- islower() → Only Lowercase Letters

text = "piyush"

print(text.islower()) # Output : True


# Example 07 :- isupper() → Only Uppercase Letters

text = "PIYUSH"

print(text.isupper()) # Output : True


# Example 08 :- isTitle() → Title Case

text = "Piyush Chakraborty"

print(text.istitle()) # Output : True


# Example 09 :- isdecimal() → Only Decimal Characters

text = "12345"

print(text.isdecimal()) # Output : True


# Example 10 :- isidentifier() → Valid Python Identifier

text = "my_variable"

print(text.isidentifier()) # Output : True


# Example 11 :- isprintable() → Printable Characters

text = "Hello\nWorld"

print(text.isprintable()) # Output : False (because of the newline character)


# Example 12 :- isascii() → ASCII Characters Only

text = "Hello"

print(text.isascii()) # Output : True (all characters are ASCII)


# Example 13 :- isnumeric() → Only Numeric Characters

text = "12345"

print(text.isnumeric()) # Output : True (all characters are numeric)


# Real-World Example 01 :- Validating User Input for a Username

user_input = input("Enter a username: ")  # User enters "Piyush123"
if user_input.isalnum():
    print("Valid username")
else:
    print("Invalid username. Only letters and numbers are allowed.")
    


# Real-World Example 02 :- Validating User Input for a Phone Number

phone_number = input("Enter your phone number: ")  # User enters "1234567890"
if phone_number.isdigit():
    print("Valid phone number")
else:
    print("Invalid phone number. Only digits are allowed.")
    
    

# Real-World Example 03 :- Validating User Input for a Password

password = input("Enter a password: ")  # User enters "P@ssw0rd"
if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
    print("Valid password")
else:
    print("Invalid password. Must be at least 8 characters long and contain uppercase, lowercase, and numeric characters.") 



# Real-World Example 04 :- Validating an Email Address

email = input("Enter your email: ")  # User enters "

if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email. Must contain '@' and end with '.com'.")
    
    

# Real-World Example 05 :- Validating a URL

url = input("Enter a URL: ")  # User enters "http://www.example.com"

if url.startswith("http://") or url.startswith("https://"):
    print("Valid URL")  
else:
    print("Invalid URL. Must start with 'http://' or 'https://'.")
    
    
# Real-World Example 06 :- Validating a Date in YYYY-MM-DD Format

date = input("Enter date: ")

if (
    len(date) == 10 and # Check length
    date[4] == "-" and  #Check for hyphens in the correct positions
    date[7] == "-" and  
    date[:4].isdigit() and  #Check if year is digits
    date[5:7].isdigit() and  #Check if month is digits
    date[8:].isdigit()        #Check if day is digits
):
    print("Valid format")   # "Valid format" (date is in the correct YYYY-MM-DD format)
else:
    print("Invalid format") # "Invalid format" (date does not meet the YYYY-MM-DD format requirements)
