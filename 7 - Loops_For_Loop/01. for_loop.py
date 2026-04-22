"""

A for loop is used to: repeat something multiple times

Instead of writing code again and again, we use a loop.

Simple meaning:

“Do this task again and again for each item”

-----------------------------------------------------------

Basic Syntax :-

for variable in iterable:
    # code
    
Here, Variable is a temporary name for the current item in the loop, and it changes with each iteration of the loop.
Iterable is a collection of items (like a list, tuple, string, etc.) that we want to loop through.

"""

# Example 01 :-

for i in range(5):
    print("Hello World")

for i in range(5):
    print(i)
    
for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)


# Example 02 :-  (Loop with a List)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
servers = ["server1", "server2", "server3"]

for server in servers:
    print("Checking:", server)
    


# Example 03 :- (Loop with a String)

name = "Hello"

for char in name:
    print(char) 
    


# Example 04 :- (Loop with a Tuple)

numbers = (1, 2, 3, 4, 5)

for num in numbers:
    print(num)
    
    
    
# Example 05 :- (Loop with a Dictionary)

person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:
    print(key, ":", person[key])
    

# Example 06 :- Uisng Enumerate() function

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
    

# Using break statement :-

for i in range(10):
    if i == 5:
        break
    print(i)
    
    
# Using continue statement :-

for i in range(10):
    if i == 2:
        continue
    print(i)    
    
    
    
# Uisng pass statement :-

for i in range(5):
    if i == 3:
        pass
    print(i)
