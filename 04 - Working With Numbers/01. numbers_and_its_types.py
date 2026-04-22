"""

Numbers are used to store numeric values. In Python, there are three types of numbers:

1. int: This type is used to store whole numbers, both positive and negative. For example: 1, -5, 0.
2. float: This type is used to store decimal numbers. For example: 3.14, -0.5, 0.0.
3. complex: This type is used to store complex numbers, which consist of a real part
and an imaginary part. For example: 2 + 3j, -1 - 4j.

You can perform various operations on numbers, such as addition, subtraction, multiplication, and division.


"""

## Main Number Types in Python :-

# Integer (int) :

a = 10
b = 20

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'int'>
print(a)  # Output: 10
print(b)  # Output: 20

c = -10 

print(type(c))  # Output: <class 'int'>
print(c)  # Output: -10


# Float (float) :

x = 3.14
y = -5.2    

print(type(x))  # Output: <class 'float'>
print(type(y))  # Output: <class 'float'>
print(x)  # Output: 3.14
print(y)  # Output: -5.2


# Complex (complex) :

z = 2 + 3j  

print(type(z))  # Output: <class 'complex'>
print(z)  # Output: (2+3j)



## Type Conversion :-

# Converting int to float

num_int = 10

num_float = float(num_int)

print(num_float)  # Output: 10.0
print(type(num_float))  # Output: <class 'float'>


# Converting float to int

num_float = 3.14

num_int = int(num_float)

print(num_int)  # Output: 3
print(type(num_int))  # Output: <class 'int'>


# Converting int to complex

num_int = 5

num_complex = complex(num_int)

print(num_complex)  # Output: (5+0j)
print(type(num_complex))  # Output: <class 'complex'>


# Converting float to complex

num_float = 2.5

num_complex = complex(num_float)

print(num_complex)  # Output: (2.5+0j)
print(type(num_complex))  # Output: <class 'complex'>


# Converting int to str

num_int = 10

num_str = str(num_int)

print(num_str)  # Output: '10'
print(type(num_str))  # Output: <class 'str'>


# Converting float to str

num_float = 3.14

num_str = str(num_float)

print(num_str)  # Output: '3.14'
print(type(num_str))  # Output: <class 'str'>


# Converting complex to str

num_complex = 2 + 3j

num_str = str(num_complex)

print(num_str)  # Output: '(2+3j)'  
print(type(num_str))  # Output: <class 'str'>


## Basic Arithmetic Operations :-

a = 10
b = 5

# Addition
add = a + b
print(add)  # Output: 15

# Subtraction
sub = a - b
print(sub)  # Output: 5

# Multiplication
mul = a * b
print(mul)  # Output: 50

# Division
div = a / b
print(div)  # Output: 2.0

# Floor Division
floor_div = a // b
print(floor_div)  # Output: 2

# Modulus
mod = a % b
print(mod)  # Output: 0

# Exponentiation
exp = a ** b
print(exp)  # Output: 100000


## Input with Numbers 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Performing addition
result = num1 + num2
print("The sum of", num1, "and", num2, "is:", result)
