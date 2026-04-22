"""

Built-in functions are predefined functions in Python that we can use directly without importing anything.


"""

## Most Important Built-in Functions :-

# 1. print() :- This function is used to display output on the console.

print("Hello World!")

# 2. input() :- This function is used to take input from the user.

name = input("Enter your name: ")
print("Hello", name)

# 3. len() :- This function is used to get the length of a string, list, tuple, etc.

my_string = "Hello World!"
print(len(my_string))

# 4. type() :- This function is used to get the type of a variable.

my_variable = 10
print(type(my_variable))

# 5. int(), float(), str() :- These functions are used to convert data types.

number = "10"
print(int(number))  # Convert string to integer

pi = 3.14
print(str(pi))  # Convert float to string

# 6. range() :- This function is used to generate a sequence of numbers.

for i in range(5):
    print(i)
    
# 7. sum() :- This function is used to get the sum of all items in an iterable.

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# 8. max() and min() :- These functions are used to get the maximum and minimum values from an iterable.

numbers = [1, 2, 3, 4, 5]

print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1

# 9. abs() :- This function is used to get the absolute value of a number.

number = -10
print(abs(number))  # Output: 10

# 10. round() :- This function is used to round a number to a specified number of decimal places.

pi = 3.14159
print(round(pi, 2))  # Output: 3.14

# 11. sorted() :- This function is used to sort an iterable in ascending order.

numbers = [5, 2, 9, 1, 5, 6]
print(sorted(numbers))  # Output: [1, 2, 5, 5, 6, 9]

# 12. reversed() :- This function is used to reverse an iterable.

my_list = [1, 2, 3, 4, 5]
print(list(reversed(my_list)))  # Output: [5, 4, 3, 2, 1]

# 13. help() :- This function is used to get help on a specific function or module.

help(print)  # Get help on the print function

# 14. pow() :- This function is used to calculate the power of a number.

base = 2
exponent = 3

print(pow(base, exponent))  # Output: 8

# 15. isinstance() :- This function is used to check if an object is an instance of a specific class or type.

number = 10

print(isinstance(number, int))  # Output: True
print(isinstance(number, str))  # Output: False
