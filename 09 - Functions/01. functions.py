"""

What is a Function? (Very Simple)

A function is:

A reusable block of code

Instead of writing code again and again → write once, reuse.

--------------------------------------

Example:

def greet():
    print("Hello, World!")
greet()  # Output: Hello, World!

In this example, we defined a function called `greet` that prints "Hello, World!" when called. 
We can call this function multiple times without having to rewrite the code inside it.

--------------------------------------

Functions can also take inputs (called parameters) and return outputs (called return values).

Example:

def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

In this example, the `add` function takes two parameters `a` and `b`, adds them together, and returns the result.

"""

# Example 01 of a simple function that takes no parameters and returns nothing

def greet():
    print("Hello, World!")
greet()  # Output: Hello, World!


# Print hello world 5 times using a function

def greet(number_of_times):
    for i in range(number_of_times):
        print("Hello, World!")  
        
greet(5)  # Output: Hello, World! (printed 5 times)


# Example 02 of a function that takes parameters and returns a value

def greet(name):
    print("Hello", name)

greet("Piyush")  # Output: Hello Piyush


def add(a, b):
    add = a + b
    return add
result = add(5, 3)
print(result)  # Output: 8


def sub(a, b):
    sub = a - b
    return sub
result = sub(5, 3)
print(result)  # Output: 2  


def sum_of_three_numbers(a, b, c):
    sum = a + b + c
    return sum
result = sum_of_three_numbers(1, 2, 3)
print(result)  # Output: 6


def area_of_rectangle(length, width):
    area = length * width
    return area

result = area_of_rectangle(5, 3)
print(result)  # Output: 15


def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

result = area_of_circle(5)
print(result)  # Output: 78.5


def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area

result = area_of_triangle(5, 3)
print(result)  # Output: 7.5


def area_of_square(side):
    area = side * side
    return area

result = area_of_square(5)
print(result)  # Output: 25


def area_of_trapezium(a, b, height):
    area = 0.5 * (a + b) * height
    return area 

result = area_of_trapezium(5, 3, 4)
print(result)  # Output: 16.0


def area_of_parallelogram(base, height):
    area = base * height
    return area 

result = area_of_parallelogram(5, 3)
print(result)  # Output: 15


def area_of_rhombus(diagonal1, diagonal2):
    area = 0.5 * diagonal1 * diagonal2
    return area

result = area_of_rhombus(5, 3)
print(result)  # Output: 7.5


def area_of_ellipse(a, b):
    pi = 3.14
    area = pi * a * b
    return area

result = area_of_ellipse(5, 3)
print(result)  # Output: 47.1


def area_of_sector(radius, angle):
    pi = 3.14
    area = 0.5 * radius * radius * (angle / 360) * pi
    return area

result = area_of_sector(5, 90)
print(result)  # Output: 19.625


# Example 03 - Default Parameters 

def greet(name="User"):
    print("Hello", name)
greet()  # Output: Hello User


# Example 04 - Variable Number of Arguments

def greet(*names):
    for name in names:
        print("Hello", name)
greet("Alice", "Bob", "Charlie")
# Output:   
# Hello Alice
# Hello Bob
# Hello Charlie


# Example 05 - Multiple Returns 

def calculate(a, b):
    sum = a + b
    product = a * b
    return sum, product

result = calculate(5, 3)
print(result)  # Output: (8, 15)


# Example 06 - Keyword Arguments 

def greet(name, greeting):
    print(greeting, name)

greet(name="Alice", greeting="Hi")  # Output: Hi Alice


def info(name, age):
    print(name, age)

info(age=25, name="Piyush") # Output: Piyush 25
