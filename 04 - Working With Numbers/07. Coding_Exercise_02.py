"""

LEVEL 1 (LOGIC – CLEAN PRACTICE SET)


"""

## Check Prime Number -> A number is prime if it is divisible only by 1 and itself

# Without def

n = int(input())

if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
        
# With def

def is_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

print(is_prime(int(input())))


## Factorial of a Number -> Multiply all numbers from 1 → n


# Without def

n = int(input())
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("Factorial:", fact)

# With def

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial(int(input())))


## Reverse a Number

# Without def

n = int(input())
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse:", rev)

# With def

def reverse(n):
    rev = 0
    
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    
    return rev

print(reverse(int(input())))


## Palindrome Number -> Reverse number → compare with original

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

# With def

def palindrome(n):
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

print(palindrome(int(input())))


## Armstrong Number -> Sum of cube of digits = number

# Without def

n = int(input())
original = n
total = 0

while n > 0:
    digit = n % 10
    total = total + digit * digit * digit
    n = n // 10

if original == total:
    print("Armstrong")
else:
    print("Not Armstrong")

# With def

def armstrong(n):
    original = n
    total = 0
    
    while n > 0:
        digit = n % 10
        total = total + digit * digit * digit
        n = n // 10
    
    if original == total:
        return "Armstrong"
    else:
        return "Not Armstrong"

print(armstrong(int(input())))


## Count Digits -> Divide by 10 until number becomes 0

# Without def

n = int(input())
count = 0

while n > 0:
    count = count + 1
    n = n // 10

print("Digits:", count)

# With def

def count_digits(n):
    count = 0
    
    while n > 0:
        count = count + 1
        n = n // 10
    
    return count

print(count_digits(int(input())))


## Fibonacci Series -> Next number = sum of previous two

# Without def

n = int(input())

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# With def

def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibonacci(int(input()))


## Sum of Digits -> Extract digits using % 10

# Without def

n = int(input())
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum:", total)

# With def

def sum_digits(n):
    total = 0
    
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    
    return total

print(sum_digits(int(input())))
