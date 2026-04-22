"""

What is *args?

*args means:

Take ANY number of inputs and store them. 

It becomes a tuple

-------------------------------

Example:

def greet(*names):
    for name in names:
        print("Hello", name)
greet("Alice", "Bob", "Charlie")

# Output:

# Hello Alice
# Hello Bob
# Hello Charlie

"""

# *args Example 01 - 

def greet(*names):
    for name in names:
        print("Hello", name)
greet("Alice", "Bob", "Charlie")


# *args Example 02 -

def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

result = add(1, 2, 3, 4, 5)
print(result)  # Output: 15


# *args Example 03 -

def concatenate(*strings):
    result = ""
    for string in strings:
        result += string
    return result
result = concatenate("Hello", " ", "World", "!")
print(result)  # Output: Hello World!


# *args Example 04 -

def average(*numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers) 

result = average(1, 2, 3, 4, 5)
print(result)  # Output: 3.0


# *args Example 05 -

def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

result = find_max(1, 2, 3, 4, 5)
print(result)  # Output: 5
