"""
    
Why Searching is Important?

In real-world:

 Check if email contains "@"
 Find word in sentence
 Cunt occurrences
 Extract positions
    
"""

# Example 01 :- find()

text = "Python Developer"

print(text.find("Dev"))  # Output: 7 (index of the first occurrence of "Dev")

# If Not Found 

print(text.find("Java"))  # Output: -1 (indicating not found)


# Example 02 :- index() -> Similar to find()

text = "Python Developer"

print(text.index("Dev"))  # Output: 7 (index of the first occurrence of "Dev")

# If Not Found 

#rint(text.index("Java"))  # Output: ValueError (indicating not found)


# Example 04 :- count() → Count Occurrences

text = "hello world"

print(text.count("l")) # 3 


text = "apple apple mango"

print(text.count("apple")) # 2


# Example 05 :- startswith() → Check Start

email = "user@gmail.com"

print(email.startswith("user"))  # Output: True


# Example 06 :- endswith() → Check End

print(email.endswith(".com"))  # Output: True


# Real-World Example 01 :- Email Validation

email = input("Enter your email: ")

if "@" in email and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")


# Real-World Example 02 :- Keyword Search in Text

text = "The quick brown fox jumps over the lazy dog."
keyword = input("Enter a keyword to search: ")

if keyword in text:
    print(f"'{keyword}' found in the text.")
else:
    print(f"'{keyword}' not found in the text.")
    
    
# Real-World Example 03 :- Count Occurrences of a Word

text = "The quick brown fox jumps over the lazy dog. The dog was not happy."

keyword = input("Enter a word to count: ")

occurrences = text.count(keyword)

print(f"'{keyword}' occurs {occurrences} times in the text.")
