"""

Operators are symbols used to perform operations on values and variables. In Python, there are several types of operators, including:

1. Arithmetic Operators: These operators are used to perform basic mathematical operations such as addition, subtraction, multiplication, and division. For example: +, -, *, /.
2. Comparison Operators: These operators are used to compare two values and return a boolean result (True or False). For example: ==, !=, >, <, >=, <=.
3. Logical Operators: These operators are used to combine multiple boolean expressions and return a boolean result. For example: and, or, not.
4. Assignment Operators: These operators are used to assign values to variables. For example: =, +=, -=, *=, /=.
5. Bitwise Operators: These operators are used to perform bitwise operations on integers. For example: &, |, ^, ~, <<, >>.
6. Identity Operators: These operators are used to compare the memory locations of two objects. For example: is, is not.
7. Membership Operators: These operators are used to check if a value is present in a sequence (like a list, tuple, or string). For example: in, not in.
8. Ternary Operator: This operator is used to evaluate a condition and return one of two values based on the result. For example: value_if_true if condition else value_if_false.   
9. Walrus Operator: This operator is used to assign a value to a variable as part of an expression. For example: variable := expression.
10. Augmented Assignment Operators: These operators are a shorthand for performing an operation and assignment in one step. For example: +=, -=, *=, /=.

"""

## Arithmetic Operators :-

# Addition (+) :

num1 = 10
num2 = 5        

result_add = num1 + num2

print(result_add)  # Output: 15

# Subtraction (-) :

result_sub = num1 - num2

print(result_sub)  # Output: 5

# Multiplication (*) :

result_mul = num1 * num2

print(result_mul)  # Output: 50

# Division (/) :

result_div = num1 / num2

print(result_div)  # Output: 2.0

# Floor Division (//) :

result_floor_div = num1 // num2

print(result_floor_div)  # Output: 2

# Modulus (%) :

result_mod = num1 % num2

print(result_mod)  # Output: 0

# Exponentiation (**) :

result_exp = num1 ** num2

print(result_exp)  # Output: 100000


## Comparison Operators :-

# Equal to (==) :

print(num1 == num2)  # Output: False

# Not equal to (!=) :

print(num1 != num2)  # Output: True

# Greater than (>) :

print(num1 > num2)  # Output: True

# Less than (<) :

print(num1 < num2)  # Output: False

# Greater than or equal to (>=) :

print(num1 >= num2)  # Output: True

# Less than or equal to (<=) :

print(num1 <= num2)  # Output: False


## Logical Operators :-

# Logical AND (and) :

print((num1 > 5) and (num2 < 10))  # Output: True

# Logical OR (or) :

print((num1 > 15) or (num2 < 10))  # Output: True

# Logical NOT (not) :

print(not (num1 > 15))  # Output: True  


## Assignment + Augmented Operators :-

# Assignment Operator (=) :

x = 10
print(x)  # Output: 10

# Augmented Assignment Operators (+=, -=, *=, /=) :

x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15

x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 12

x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 24

x /= 4  # Equivalent to x = x / 4
print(x)  # Output: 6.0


## Membership Operators :-

# Membership Operator (in) :

my_list = [1, 2, 3, 4, 5]

print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False


# Membership Operator (not in) :

print(3 not in my_list)  # Output: False
print(6 not in my_list)  # Output: True     


## Identity Operators :-

# Identity Operator (is) :

a = [1, 2, 3]
b = a

print(a is b)  # Output: True


# Identity Operator (is not) :

c = [1, 2, 3]

print(a is not c)  # Output: True


## Ternary Operator :-

age = 18

status = "Adult" if age >= 18 else "Minor"

print(status)  # Output: Adult
