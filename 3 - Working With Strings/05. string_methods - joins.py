"""
join() = Used to combine multiple strings into one string

----------------------------------------------

Syntax :-       

separator.join(iterable)

separator → string that will be inserted between the elements of the iterable
iterable → a collection of strings (like list, tuple, etc.) that you want to join together

----------------------------------------------

Basic Example :-

words = ["Hello", "World"]  
sentence = " ".join(words)
print(sentence)  # "Hello World"

"""

## Different Separators :-

# Joining with a Space

words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)  # "Python is easy"


# Joining with a Comma

words = ["apple", "banana", "cherry"]
csv = ",".join(words)
print(csv)  # "apple,banana,cherry"


# Joining with a Dash 

words = ["2024", "06", "30"]
date = "-".join(words)
print(date)  # "2024-06-30"


# Joining with an Empty String

words = ["H", "e", "l", "l", "o"]
word = "".join(words)   
print(word)  # "Hello"


# Joining with a Custom Separator

words = ["Piyush", "Kumar", "Sharma"]
full_name = " | ".join(words)
print(full_name)  # "Piyush | Kumar | Sharma"


## Real-World Examples :-

# Example 01 :- Create Email Address


username = "piyush"
domain = "gmail.com"    
email = "@".join([username, domain])
print(email)  # piyush@gmail.com    


# Example 02 :- Create a File Path

folders = ["home", "user", "documents"]
file_path = "/".join(folders)
print(file_path)  # "home/user/documents"


# Example 03 :- Create a CSV String

data = ["John", "Doe", "30", "Engineer"]
csv_string = ",".join(data)
print(csv_string)  # "John,Doe,30,Engineer" 


# Example 04 :- Create a URL

protocol = "https"
domain = "www.example.com"
path = "page"
url = "/".join([protocol + ":", domain, path])
print(url)  # "https://www.example.com/page"


# Example 05 :- Create a Sentence from Words

words = ["Python", "is", "a", "great", "language"]
sentence = " ".join(words)
print(sentence)  # "Python is a great language"
