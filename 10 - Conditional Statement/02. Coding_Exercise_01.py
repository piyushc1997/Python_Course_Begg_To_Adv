"""

LEVEL 1 — CONDITIONAL STATEMENTS (FOUNDATION)


"""

## Positive, Negative, or Zero

def check_number(num):
    
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_number(int(input("")))


## Even or Odd

def even_odd(n):
    
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(int(input()))


## Eligible to Vote

def check_vote(age):
    
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")

check_vote(int(input()))


## Largest of Two Numbers

def largest(a, b):
    
    if a > b:
        print(a)
    else:
        print(b)

largest(int(input()), int(input()))


## Divisible by 5

def check_divisible(n):
    
    if n % 5 == 0:
        print("Divisible")
    else:
        print("Not Divisible")

check_divisible(int(input()))


## Number is Greater than 10 or Not

def check_num(n):
    
    if n > 10:
        print("Greater than 10")
    else:
        print("Less or Equal to 10")

check_num(int(input()))

## Check Equal or Not

def check_equal(a, b):
    
    if a == b:
        print("Equal")
    else:
        print("Not Equal")

check_equal(int(input()), int(input()))


## Check Pass or Fail

def result(marks):
    
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

result(int(input()))


## Check Character is Alphabet or Not

def check_char(ch):
    
    if ch.isalpha():
        print("Alphabet")
    else:
        print("Not Alphabet")

check_char(input())


## Check Number is Single Digit

def single_digit(n):
    
    if -9 <= n <= 9:
        print("Single Digit")
    else:
        print("Not Single Digit")

single_digit(int(input()))
