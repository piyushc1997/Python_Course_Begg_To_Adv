"""

Rounding numbers is a common task in programming, and Python provides several built-in functions to help with this. 

The most commonly used functions for rounding are `round()`, `floor()`, and `ceil()`.   

Why Rounding is Important?

In real-world:

Prices → ₹99.456 → ₹99.46
Marks → 89.6 → 90
Reports → clean values

1. `round()`: This function rounds a number to a specified number of decimal places. If no decimal places are specified, it rounds to the nearest integer. For example: `round(3.14159, 2)` will return `3.14`. 
2. `floor()`: This function rounds a number down to the nearest integer. For example: `math.floor(3.7)` will return `3`.
3. `ceil()`: This function rounds a number up to the nearest integer. For example: `math.ceil(3.2)` will return `4`.

"""

## Rounding with `round()` :- It means use for normal rounding to the nearest integer or to a specified number of decimal places.

# Rounding to the nearest integer

num1 = 3.6

rounded_num1 = round(num1)

print(rounded_num1)  # Output: 4


# Rounding to a specific number of decimal places

num2 = 3.14159

rounded_num2 = round(num2, 2)

print(rounded_num2)  # Output: 3.14


## Rounding with `floor()` :- Alwasys rounds down to the nearest integer

# Importing the math module to use floor function

import math

num3 = 3.7

floored_num3 = math.floor(num3)

print(floored_num3)  # Output: 3


# Example 02 :-

num4 = 5.6

floored_num4 = math.floor(num4)

print(floored_num4)  # Output: 5


## Rounding with `ceil()` :- Always rounds up to the nearest integer

# Example 01 :-

num5 = 3.2

ceiled_num5 = math.ceil(num5)

print(ceiled_num5)  # Output: 4


# Example 02 :-

num6 = 10.7

ceiled_num6 = math.ceil(num6)

print(ceiled_num6)  # Output: 11


## Real-world Applications of Rounding :-

# Rounding Prices

price = 99.456

rounded_price = round(price, 2)

print(rounded_price)  # Output: 99.46


# Rounding Marks

marks = 89.6

rounded_marks = round(marks)

print(rounded_marks)  # Output: 90


# Ceiling the number of pages required to print a report

pages = 250

pages_per_sheet = 2

sheets_required = math.ceil(pages / pages_per_sheet)

print(sheets_required)  # Output: 125


# Ceiling the number of boxes required to pack items

items = 53

items_per_box = 10

boxes_required = math.ceil(items / items_per_box)

print(boxes_required)  # Output: 6


# Flooring the number of hours required to complete a task

total_hours = 7.5

hours_per_day = 8

days_required = math.floor(total_hours / hours_per_day)

print(days_required)  # Output: 0


# Flooring the number of weeks required to complete a project

total_days = 45

days_per_week = 7

weeks_required = math.floor(total_days / days_per_week)

print(weeks_required)  # Output: 6
