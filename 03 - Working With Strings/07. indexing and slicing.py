"""

Indexing means accessing a single character from a string. 


"""

# Example 01 :-

name = "Piyush"

print(name[0])  # "P"
print(name[5])  # "h"


# Example 02 :- Negative Indexing

name = "Piyush"

print(name[-1])  # "h"
print(name[-6])  # "P"


"""

Slicing means accessing a substring (a portion of the string) by specifying a range of indices.

Syntax :-

string[start : end : step]

start → The starting index of the slice (inclusive)
end → The ending index of the slice (exclusive) 
step → The step size (optional, default is 1)

"""

# Example 01 :-

name = "Piyush"

print(name[0:3])   # Piy
print(name[1:4])   # iyu


## Default Values in Slicing :-

# Star Omitted :-

name = "Piyush"
print(name[:3])   # Piy


# End Omitted :-

name = "Piyush"
print(name[3:6])   # ush


# Both Start and End Omitted :-

name = "Piyush"
print(name[:])   # Piyush   


## Step in Slicing :-

# Example 02 :-

name = "Piyush"
print(name[0:6:2])   # Pys


# Example 03 :-

name = "Piyush"
print(name[1:6:2])   # iu


# Example 04 :-

name = "Piyush"
print(name[::2])   # Pys


# Example 05 :-

name = "Piyush"
print(name[1::2])   # iu


# Example 06 :- Reverse a String using Slicing

name = "Piyush"
print(name[::-1])   # hsuyiP


# Real-World Example 01 :-Get first name

full_name = "Piyush Chakraborty"
first_name = (full_name[:6])
print(first_name)  # Piyush


# Real-World Example 02 :- Get last name

full_name = "Piyush Chakraborty"
last_name = (full_name[7:18])
print(last_name)  # Chakraborty


# Real-World Example 03 :- Get initials

full_name = "Piyush Chakraborty"
initials = full_name[0] + full_name[7]  
print(initials)  # PC


# Real-World Example 04 :- Get full name

first_name = "Piyush"
last_name = "Chakraborty"
print(full_name)  # Piyush Chakraborty


# Real-World Example 05 :- Get domain from email

email = "piyush@gmail.com"
domain = email[7:]
print(domain) # gmail.com
