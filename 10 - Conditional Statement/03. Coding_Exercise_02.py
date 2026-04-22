"""

LEVEL 2 — CONDITIONAL STATEMENTS (LOGIC BUILDING)


"""

## Largest of Three Numbers

def largest(a, b, c):
    
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)

largest(int(input()), int(input()), int(input()))


## Grade System

def grade(marks):
    
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 50:
        print("C")
    else:
        print("Fail")

grade(int(input()))


## Leap Year

def leap(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")

leap(int(input()))


## Check Number Range

def check_range(num):
    
    if 1 <= num <= 100:
        print("In range")
    else:
        print("Out of range")

check_range(int(input()))


## Divisible by 3, 5 or Both

def check_div(n):
    
    if n % 3 == 0 and n % 5 == 0:
        print("Both")
    elif n % 3 == 0:
        print("3")
    elif n % 5 == 0:
        print("5")
    else:
        print("None")

check_div(int(input()))


## Character Type Check

def char_type(ch):
    
    if ch.isalpha():
        print("Alphabet")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special")

char_type(input())


## Simple Calculator

def calc(a, b, op):
    
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Invalid")

calc(int(input()), int(input()), input())


## Temperature Category

def temp_check(t):
    
    if t > 30:
        print("Hot")
    elif t > 25:
        print("Warm")
    else:
        print("Cold")

temp_check(float(input()))


## Password Strength (Basic)

def password(pwd):
    
    if len(pwd) >= 8:
        print("Strong")
    else:
        print("Weak")

password(input())


## Day of Week (Number Input)

def day_name(d):
    
    if d == 1:
        print("Monday")
    elif d == 2:
        print("Tuesday")
    elif d == 3:
        print("Wednesday")
    elif d == 4:
        print("Thursday")
    elif d == 5:
        print("Friday")
    elif d == 6:
        print("Saturday")
    elif d == 7:
        print("Sunday")
    else:
        print("Invalid")

day_name(int(input()))
