""" 
input() is used to take input from the user.

Basic Example:

name = input("Enter your name: ")
print(name)

Output:

Enter your name: Piyush
Piyush

-----------------------------------------------

How input() Works?

Program pauses
Waits for user input
User types something
Value is stored in a variable

"""

# Different Types of Input :-

# (A) String Input

name = input("Enter your name: ")
print(f"Hello, {name}!")  # Output: Hello, Piyush! (if user types Piyush)

# (B) Integer Input

age = int(input("Enter your age: "))
print(f"You are {age} years old.")  # Output: You are 25 years old. (if user types 25)

# (C) Float Input

height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")  # Output: Your height is 1.75 meters. (if user types 1.75)

# (D) Boolean Input

is_student = input("Are you a student? (yes/no): ").lower() == "yes"
print(f"Is student: {is_student}")  # Output: Is student: True (if user types yes) 

# Real-World Example

name = input(f"Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")  # Output  Hello, Piyush! You are 25 years old. (if user types Piyush and 25)

# Multiple Inputs in One Line (Advanced Beginner) 

name, age = input("Enter your name and age separated by space: ").split() 
age = int(age)  # Convert age to integer
print(f"Hello, {name}! You are {age} years old.")  # Output: Hello, Piyush! You are 25 years old. (if user types Piyush 25)

# Converting Input to Desired Type (Important)

number = int(input("Enter a number: "))
print(f"You entered: {number}")  # Output: You entered: 42 (if user types 42)   

a, b = map(int, input("Enter numbers: ").split())
print(f"You entered: {a} and {b}")  # Output: You entered: 10 and 20 (if user types 10 20)

# Real-World DevOps Use Case (Simple Idea)

username = input("Enter your username: ")
password = input("Enter your password: ")
print(f"Username: {username}, Password: {password}")  # Output: Username: admin, Password: secret (if user types admin and secret)


server = input("Enter server name: ")
env = input("Enter environment (dev/prod): ")

print(f"Deploying to {server} in {env} environment")  # Output: Deploying to myserver in prod environment (if user types myserver and prod)
