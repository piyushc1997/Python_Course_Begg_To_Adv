"""
    
Why Removing Spaces is Important?

In real-world:

User input often has extra spaces
Data from files/APIs may be messy
Validation fails due to spaces
    
----------------------------------------------

Methods to Remove Spaces:

1. str.strip() - Removes leading and trailing spaces
2. str.lstrip() - Removes leading spaces
3. str.rstrip() - Removes trailing spaces
4. str.replace() - Can remove all spaces by replacing them with an empty string

----------------------------------------------

"""

# Example 01 :- Using str.strip()

name = "   Piyush   "

clean_name = name.strip()

print(clean_name)  # "Piyush" (leading and trailing spaces removed)


# Example 01.1 :- Real Example of str.strip() with User Input

user_input = input("Enter your name: ")  # User enters "   Piyush   "

clean_input = user_input.strip()    

print(f"Hello, {clean_input}!")  # "Hello, Piyush!" (spaces removed)


# Example 02 :- Using str.lstrip()

name = "   Piyush   "

clean_name = name.lstrip()

print(clean_name)  # "Piyush   " (only leading spaces removed)


#  Example 03 :- Using str.rstrip()

name = "   Piyush   "

clean_name = name.rstrip()

print(clean_name)  # "   Piyush" (only trailing spaces removed)


# Example 04 :- Using str.replace() to Remove All Spaces

text = " Hello World "

clean_text = text.replace(" ", "")

print(clean_text)  # "HelloWorld" (all spaces removed)


# Example 05 :- Using str.replace() to Remove All Spaces from User Input

user_input = input("Enter a sentence: ")  # User enters " Hello World "

clean_input = user_input.replace(" ", "")

print(f"Cleaned input: {clean_input}")  # "Cleaned input: HelloWorld" (all spaces removed)


# Example 06 :- Removing Multiple Spaces with str.replace()


text = " Hello    World "

clean_text = text.replace(" ", "")

print(clean_text)  # "HelloWorld" (all spaces removed, including multiple spaces)


## Removing Specific Character :-

# Example 07 :- Remove Hyphens from a String

text = "2024-06-30"

clean_text = text.replace("-", "")

print(clean_text)  # "20240630" (hyphens removed)


# Example 08 :- Remove Underscores from a String

text = "Hello_World"

clean_text = text.replace("_", "")

print(clean_text)  # "HelloWorld" (underscores removed)


# Example 09 :- Remove Newline Characters from a String

text = "Hello\nWorld"

clean_text = text.replace("\n", "")

print(clean_text)  # "HelloWorld" (newline characters removed)


# Real-World Example 01 :- Removing Spaces from User Input for Validation

user_input = input("Enter your username: ")  # User enters "   piyush   "

clean_username = user_input.strip()

print(f"Your username is: '{clean_username}'")  # "Your username is: 'piyush'" (spaces removed for validation)


# Real-World Example 02 :- Remove unwanted characters from a messy phone number

phone_number = "+49 (176) 123 - 4567"

clean_number = phone_number.replace("+", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")

print(clean_number)  # "491761234567" (all unwanted characters removed, leaving only digits)


# Real-World Example 03 :- Removing Extra Spaces from a CSV String

csv = " apple, banana , cherry "

clean_csv = csv.replace(" ", "")

print(clean_csv)  # "apple,banana,cherry" (all spaces removed from the CSV string)


# Real-World Example 04 :- Removing Spaces from a URL

url = " http://www.example.com/page "

clean_url = url.strip()

print(clean_url)  # "http://www.example.com/page" (leading and trailing spaces removed from the URL)
