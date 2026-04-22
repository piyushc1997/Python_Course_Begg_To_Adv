"""

split() method is used to split a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace.

-----------------------------------------------

Syntax :-

string.split(separator, maxsplit)

separator → The delimiter string (optional, default is whitespace)
maxsplit → Maximum number of splits to perform (optional, default is -1, which means no limit)

-----------------------------------------------

Basic Example :-

text = "Hello World"
words = text.split()
print(words)  # ['Hello', 'World']


"""

# Example 01 :-

text = "Hello World Python"

words = text.split()

print(words)  # ['Hello', 'World', 'Python']


## Split with a Custom Separator

# Example 02 :- Split with a Comma

csv = "apple,banana,cherry"
fruits = csv.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']


# Example 03 :- Split with a Dash

date = "2024-06-30"
date_parts = date.split("-")
print(date_parts)  # ['2024', '06', '30']


# Example 04 :- Split with a Custom Separator

text = "Piyush | Kumar | Sharma"
name_parts = text.split(" | ")  
print(name_parts)  # ['Piyush', 'Kumar', 'Sharma']


# Example 05 :- Split with maxsplit

text = "apple,banana,cherry,grape"
fruits = text.split(",", 2)
print(fruits)  # ['apple', 'banana', 'cherry,grape']    


# Example 06 :- Split with No Separator (Splitting on Whitespace)

text = "   Hello   World   "
words = text.split()
print(words)  # ['Hello', 'World'] (leading and trailing whitespace is ignored, and multiple spaces are treated as a single separator)


## Real-World Examples :-

# Example 01 :- Take Full Name → First & Last Name

name = "Piyush Chakraborty"

first, last = name.split()

print(first)  # "Piyush"
print(last) # "Chakraborty"


# Example 02 :- Extract Email Parts

email = "piyush@gmail.com"

username, domain = email.split("@")

print(username) # "piyush"
print(domain)   # "gmail.com"


# Example 03 :- Parse a CSV Line

csv_line = "John,Doe,30,Engineer"
name, surname, age, profession = csv_line.split(",")
print(name)       # "John"
print(surname)    # "Doe"
print(age)        # "30"
print(profession) # "Engineer"


# Example 04 :- Split a URL into Components

url = "https://www.example.com/path/to/page?query=python"
protocol, rest = url.split("://")
domain, path_query = rest.split("/", 1)
print(protocol)   # "https"
print(domain)     # "www.example.com"
print(path_query) # "path/to/page?query=python"


# Example 05 :- Split a Log Entry

log_entry = "ERROR: 2024-06-01 12:00:00 - Something went wrong!"
log_level, timestamp_message = log_entry.split(": ", 1)
timestamp, message = timestamp_message.split(" - ", 1)
print(log_level)  # "ERROR"
print(timestamp)  # "2024-06-01 12:00:00"
print(message)    # "Something went wrong!"


# Example 06 :- Split a Date String

date = "2024-06-30"
year, month, day = date.split("-")
print(year)   # "2024"
print(month)  # "06"
print(day)    # "30"
