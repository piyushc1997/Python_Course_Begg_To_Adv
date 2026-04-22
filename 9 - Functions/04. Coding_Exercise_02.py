"""
LEVEL 1: BASIC (MUST MASTER)

# Find Maximum of 2 Numbers
# Check Even or Odd
# Sum of Digits
# Calculate the Area of a Circle
# Calculate the Area of a Rectangle
# Calculate the Area of a Triangle
# Calculate the Area of a Square
# Calculate the Area of a Trapezium
# Calculate the Sum of Squares of First n Even Numbers
# Calculate the Sum of Cubes of First n Natural Numbers
# Calculate the Power of a Number
# Swap Two Numbers
# Find Minimum of 2 Numbers
# Check Positive / Negative / Zero
# Largest of 3 Numbers
# Simple Interest
# Compound Interest
# Convert Celsius to Fahrenheit
# Convert Fahrenheit to Celsius
# Convert Kilometers to Miles
# Convert Miles to Kilometers
# Convert Hours to Minutes
# Convert Minutes to Hours
# Check Divisible by 5 and 11
# Number is Multiple of Another
# Leap Year
# Calculate the Area of a Parallelogram
# Calculate the Area of a Rhombus
# Calculate the Area of an Ellipse
# Calculate the Area of a Sector

"""

### Solutions:

## Find Maximum of 2 Numbers

# with def()

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Max:", find_max(a, b))

# without def()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Max:", a)
else:
    print("Max:", b)


## Solution 02 - Check Even or Odd

# with def()

def check_even_odd(n):
    
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))

print(check_even_odd(n))

# without def()

n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


## Solution 03 - Sum of Digits

# with def()

def sum_digits(n):
    total = 0
    for digit in str(n):
        total = total + int(digit)
    return total

n = int(input("Enter number: "))
print("Sum:", sum_digits(n))

# without def()

n = input("Enter number: ")
total = 0

for digit in n:
    total = total + int(digit)
print("Sum:", total)


## Solution 04 - Calculate the Area of a Circle

# with def()

def area_circle(r):
    area = 3.14 * r * r
    return area

r = float(input("Enter radius: "))
print("Area:", area_circle(r))

# without def()

r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area:", area)


## Solution 05 - Calculate the Area of a Rectangle

# with def()

def area_rectangle(l, b):
    return l * b

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Area:", area_rectangle(l, b))

# Without def

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
area = l * b
print("Area:", area)


## Solution 06 - Calculate the Area of a Triangle

# with def()

def area_triangle(b, h):
    return 0.5 * b * h

b = int(input("Enter base: "))
h = int(input("Enter height: "))
print("Area:", area_triangle(b, h))

# without def()

b = int(input("Enter base: "))
h = int(input("Enter height: "))
area = 0.5 * b * h
print("Area:", area)


## Solution 07 - Calculate the Area of a Square

# with def()

def area_square(s):
    return s * s

s = int(input("Enter side: "))
print("Area:", area_square(s))

# without def()

s = int(input("Enter side: "))
area = s * s
print("Area:", area)


## Solution 08 - Calculate the Area of a Trapezium

# With def

def area_trap(a, b, h):
    return 0.5 * (a + b) * h

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
h = int(input("Enter height: "))
print("Area:", area_trap(a, b, h))

# Without def

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
h = int(input("Enter height: "))
area = 0.5 * (a + b) * h
print("Area:", area)


## Solution 09 - Calculate the Sum of Squares of First n Even Numbers

# With def

def sum_squares(n):
    total = 0
    for i in range(1, n+1):
        even = 2 * i
        total = total + even * even
    return total

n = int(input())
print("Sum:", sum_squares(n))

# Without def

n = int(input())
total = 0

for i in range(1, n+1):
    even = 2 * i
    total = total + even * even

print("Sum:", total)


## Solution 10 - Calculate the Sum of Cubes of First n Natural Numbers

# With def

def sum_cubes(n):
    total = 0
    for i in range(1, n+1):
        total = total + i*i*i
    return total

n = int(input())
print("Sum:", sum_cubes(n))

# Without def

n = int(input())
total = 0

for i in range(1, n+1):
    total = total + i*i*i

print("Sum:", total)


## Solution 11 - Calculate the Power of a Number

# With def
def power(a, b):
    return a ** b

a = int(input())
b = int(input())
print("Power:", power(a, b))

# Without def
a = int(input())
b = int(input())

result = a ** b
print("Power:", result)


## Solution 12 - Swap Two Numbers

# With def

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = swap(a, b)
print("After swapping: a =", a, "b =", b)

# Without def

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping: a =", a, "b =", b)


## Solution 13 - Find Minimum of 2 Numbers

# With def

def find_min(a, b):
    if a < b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Minimum:", find_min(a, b))

# Without def

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print("Minimum:", a)
else:
    print("Minimum:", b)
    
    
## Solution 14 - Check Positive / Negative / Zero

# With def

def check_sign(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
    
n = int(input("Enter number: "))
print(check_sign(n))

# Without def

n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
    
    
## Solution 15 - Largest of 3 Numbers

# With def

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest:", largest_of_three(a, b, c))

# Without def

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
    
    
## Solution 16 - Simple Interest

# With def

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

print("Simple Interest:", simple_interest(p, r, t))

# Without def

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

simple_interest = (p * r * t) / 100
print("Simple Interest:", simple_interest)


## Solution 17 - Compound Interest

# With def

def compound_interest(p, r, t):
    return p * (1 + r / 100) ** t - p

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

print("Compound Interest:", compound_interest(p, r, t))

# Without def

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

compound_interest = p * (1 + r / 100) ** t - p
print("Compound Interest:", compound_interest)


## Solution 18 - Convert Celsius to Fahrenheit -> Formula: (C × 9/5) + 32

# With def

def c_to_f(c):
    return (c * 9/5) + 32

c = float(input("Enter Celsius: "))
print("Fahrenheit:", c_to_f(c))

# Without def

c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)



## Solution 19 - Convert Fahrenheit to Celsius -> Formula: (F − 32) × 5/9

# With def

def f_to_c(f):
    return (f - 32) * 5/9

f = float(input("Enter Fahrenheit: "))
print("Celsius:", f_to_c(f))

# Without def

f = float(input("Enter Fahrenheit: "))
c = (f - 32) * 5/9
print("Celsius:", c)


## Convert Kilometers to Miles -> 1 km = 0.621 km (approx)

# With def

def km_to_miles(km):
    return km * 0.621

km = float(input("Enter km: "))
print("Miles:", km_to_miles(km))

# Without def

km = float(input("Enter km: "))
miles = km * 0.621
print("Miles:", miles)


## Convert Miles to Kilometers -> 1 mile = 1.609 km

# With def

def miles_to_km(m):
    return m * 1.609

m = float(input("Enter miles: "))
print("Kilometers:", miles_to_km(m))

# Without def

m = float(input("Enter miles: "))
km = m * 1.609
print("Kilometers:", km)


## Convert Hours to Minutes

# With def

def hours_to_minutes(h):
    return h * 60

h = int(input("Enter hours: "))
print("Minutes:", hours_to_minutes(h))

# Without def

h = int(input("Enter hours: "))
minutes = h * 60
print("Minutes:", minutes)


## Convert Minutes to Hours

# With def

def minutes_to_hours(m):
    return m / 60

m = int(input("Enter minutes: "))
print("Hours:", minutes_to_hours(m))

# Without def

m = int(input("Enter minutes: "))
hours = m / 60
print("Hours:", hours)


##  Check Divisible by 5 and 11

# With def

def check_divisible(n):
    if n % 5 == 0 and n % 11 == 0:
        return "Divisible"
    else:
        return "Not Divisible"

print(check_divisible(int(input())))

# Without def

n = int(input())

if n % 5 == 0 and n % 11 == 0:
    print("Divisible")
else:
    print("Not Divisible")
    
    
## Number is Multiple of Another

# With def

def is_multiple(a, b):
    if a % b == 0:
        return "Yes"
    else:
        return "No"

a = int(input())
b = int(input())
print(is_multiple(a, b))

# Without def

a = int(input())
b = int(input())

if a % b == 0:
    print("Yes")
else:
    print("No")
    
    
## Leap Year -> divisible by 4 AND not by 100 OR divisible by 400

# With def
def leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not Leap Year"

print(leap_year(int(input())))

# Without def

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
    
    
## Area of Parallelogram -> base × height

# With def

def area_para(b, h):
    return b * h

b = int(input())
h = int(input())
print("Area:", area_para(b, h))

# Without def

b = int(input())
h = int(input())

area = b * h
print("Area:", area)


## Area of Rhombus -> (d1 × d2) / 2

# With def
def area_rhombus(d1, d2):
    return (d1 * d2) / 2

d1 = int(input())
d2 = int(input())
print("Area:", area_rhombus(d1, d2))

# Without def
d1 = int(input())
d2 = int(input())

area = (d1 * d2) / 2
print("Area:", area)


## Area of Ellipse -> π × a × b

# With def

def area_ellipse(a, b):
    return 3.14 * a * b

a = float(input())
b = float(input())
print("Area:", area_ellipse(a, b))

# Without def

a = float(input())
b = float(input())

area = 3.14 * a * b
print("Area:", area)


## Area of Sector -> (θ/360) × πr²

# With def

def area_sector(r, theta):
    return (theta / 360) * 3.14 * r * r

r = float(input())
theta = float(input())
print("Area:", area_sector(r, theta))

# Without def

r = float(input())
theta = float(input())

area = (theta / 360) * 3.14 * r * r
print("Area:", area)
