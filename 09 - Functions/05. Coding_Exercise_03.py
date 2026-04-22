"""

LEVEL 2 (INTERMEDIATE)


"""

## Check Prime Number -> A number is prime if it has only 2 factors: 1 and itself -> Logic:
## Loop from 2 to n-1
## If divisible → NOT prime

# With def

def is_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

n = int(input("Enter number: "))
print(is_prime(n))

# Without def
n = int(input("Enter number: "))

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
        
        
## Factorial of a Number -> Example: 5! = 5×4×3×2×1

# With def

def factorial(n):
    factorial = 1
    
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

n = int(input("Enter number: "))

print("Factorial:", factorial(n))

# Without def

n = int(input("Enter number: "))
factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print("Factorial:", factorial)


## Fibonacci Series -> 0, 1, 1, 2, 3, 5...

# With def

def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter number: "))
fibonacci(n)

# Without def

n = int(input("Enter number: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    
    
## Reverse a Number -> 123 → 321

# With def

def reverse_number(n):
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    
    return rev

n = int(input("Enter number: "))
print("Reverse:", reverse_number(n))

# Without def

n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse:", rev)


## Palindrome Number -> 121 → same when reversed

# With def

def is_palindrome(n):
    original = n
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    
    if original == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"

n = int(input())
print(is_palindrome(n))

# Without def

n = int(input())
original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
## Armstrong Number -> 153 → 1³ + 5³ + 3³ = 153 -> Sum of cube of digits

# With def

def is_armstrong(n):
    original = n
    total = 0
    
    while n > 0:
        digit = n % 10
        total = total + digit**3
        n = n // 10
    
    if original == total:
        return "Armstrong"
    else:
        return "Not Armstrong"

n = int(input())
print(is_armstrong(n))

# Without def

n = int(input())
original = n
total = 0

while n > 0:
    digit = n % 10
    total = total + digit**3
    n = n // 10

if original == total:
    print("Armstrong")
else:
    print("Not Armstrong")
    
    
## Count Digits -> Keep dividing by 10

# With def

def count_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

print(count_digits(int(input())))

# Without def

n = int(input())
count = 0

while n > 0:
    count = count + 1
    n = n // 10

print("Digits:", count)


## Sum of Even and Odd Numbers (1 to n) -> Use loop and check % 2

# With def

def sum_even_odd(n):
    even = 0
    odd = 0
    
    for i in range(1, n+1):
        if i % 2 == 0:
            even = even + i
        else:
            odd = odd + i
    
    return even, odd

n = int(input())
e, o = sum_even_odd(n)

print("Even Sum:", e)
print("Odd Sum:", o)

# Without def
n = int(input())
even = 0
odd = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print("Even Sum:", even)
print("Odd Sum:", odd)


## Multiplication Table -> Loop from 1 to 10

# With def

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

table(int(input()))

# Without def

n = int(input())

for i in range(1, 11):
    print(n, "x", i, "=", n*i)
