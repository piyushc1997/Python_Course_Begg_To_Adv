"""
Replace method is used to replace a specified phrase with another specified phrase. It returns a new string with the replaced phrase.

Simple definition:

Replace old text → with new text

----------------------------------------------
Syntax :-

string.replace(old, new, count)

old → text to find
new → text to replace with

----------------------------------------------

Basic Example :-

text = "Hello World"

new_text = text.replace("World", "Python")

print(new_text)  # "Hello Python"


"""

# Example 01 :-

text = "Hello World"

text = text.replace("World", "Piyush")
print(text)


# Example 02 :- Replace Multiple Occurrences of a Substring

text = "apple apple apple"

print(text.replace("apple", "mango"))  # "mango mango mango"

text = "The quick brown fox jumps over the lazy dog. The dog was not happy."
new_text = text.replace("dog", "cat")
print(new_text)  # "The quick brown fox jumps over the lazy cat. The cat was not happy."


# Example 03 :- Replace Only the First Occurrence

text = "apple apple apple"
new_text = text.replace("apple", "mango", 1)
print(new_text)  # "mango apple apple"


# Example 04 :- Case-Sensitive Replacement

text = "Hello World"
new_text = text.replace("world", "Python")
print(new_text)  # "Hello World" (no change because "world" is not found due to case sensitivity)


# Example 05 :- Replacing Substrings with Empty Strings (Removing Substrings)

text = "Hello World"
new_text = text.replace("World", "")
print(new_text)  # "Hello " (note the space after "Hello")


# Example 06 :- Replacing Special Characters

text = "Hello, World!"
new_text = text.replace(",", "")    
print(new_text)  # "Hello World!" (comma removed)


# Example 07 :- Replacing Newline Characters

text = "Hello\nWorld"
new_text = text.replace("\n", " ")  
print(new_text)  # "Hello World" (newline replaced with space)      

# Example 08 :- Replacing Tabs

text = "Hello\tWorld"
new_text = text.replace("\t", " ")
print(new_text)  # "Hello World" (tab replaced with space)


# Example 09 :- Replacing Multiple Different Substrings

text = "The quick brown fox jumps over the lazy dog."
new_text = text.replace("fox", "cat").replace("dog", "hamster")
print(new_text)  # "The quick brown cat jumps over the lazy hamster."


# Example 10 :- Convert the messy phone number to a clean number format with only digits.

phone_number = "+49 (176) 123 - 4567"

clean_number = phone_number.replace("+", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")


## Some Real-World Examples :-

# Email Domain Change

email = "user@yahoo.com"

new_email = email.replace("yahoo.com", "gmail.com")

print(new_email)


# URL Update

url = "http://www.oldsite.com/page"
new_url = url.replace("oldsite.com", "newsite.com")
print(new_url)  # "http://www.newsite.com/page"


# Log File Cleanup

log_entry = "ERROR: 2024-06-01 12:00:00 - Something went wrong!"
clean_log_entry = log_entry.replace("ERROR: ", "")
print(clean_log_entry)  # "2024-06-01 12:00:00 - Something went wrong!" 

# Data Sanitization

user_input = "   Hello World!   "
sanitized_input = user_input.replace(" ", "")   
print(sanitized_input)  # "HelloWorld!" (all spaces removed)


# Removing HTML Tags

html_string = "<p>This is a paragraph.</p>"
clean_string = html_string.replace("<p>", "").replace("</p>", "")
print(clean_string)  # "This is a paragraph." (HTML tags removed)


# Replacing Placeholders in a Template

template = "Dear {name}, your order #{order_id} has been shipped."
personalized_message = template.replace("{name}", "Piyush").replace("{order_id}", "12345")
print(personalized_message)  # "Dear Piyush, your order #12345 has been shipped."
