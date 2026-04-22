"""

LEVEL 4 — CONDITIONAL + LOOPS (REAL INTERVIEW PATTERNS)


"""

## Count Even and Odd Numbers (User Input List)

def count_even_odd():
    
    nums = list(map(int, input("Enter numbers (space separated): ").split()))

    even = 0
    odd = 0

    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even:", even)
    print("Odd:", odd)

count_even_odd()


## Sum of Even Numbers

def sum_even():
    
    nums = list(map(int, input().split()))
    total = 0

    for n in nums:
        if n % 2 == 0:
            total += n

    print("Sum of even:", total)

sum_even()


## Find Largest Number

def find_max():

    nums = list(map(int, input().split()))

    max_val = nums[0]

    for n in nums:
        if n > max_val:
            max_val = n

    print("Max:", max_val)

find_max()


## Count Vowels in String

def count_vowels():
    
    s = input("Enter string: ")
    count = 0

    for ch in s:
        if ch.lower() in "aeiou":
            count += 1

    print("Vowels:", count)

count_vowels()


## Perfect Number (VERY IMPORTANT) -> A number is perfect if sum of its divisors = number -> Example: 6 → 1+2+3 = 6

def perfect_number():
    
    n = int(input("Enter number: "))
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        print("Perfect Number")
    else:
        print("Not Perfect")

perfect_number()


## Print All Divisors

def divisors():
    
    n = int(input())

    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")

divisors()


## Count Number of Divisors

def count_divisors():
    
    n = int(input())
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    print("Total divisors:", count)

count_divisors()


## First and Last Digit (Number)

def first_last_digit():
    
    n = int(input())

    last = n % 10

    while n >= 10:
        n //= 10

    first = n

    print("First:", first)
    print("Last:", last)

first_last_digit()


## First and Last Character (String)

def first_last_char():
    
    s = input()

    if len(s) > 0:
        print("First:", s[0])
        print("Last:", s[-1])
    else:
        print("Empty string")

first_last_char()


## Reverse a Number

def reverse_number():
    
    n = int(input())
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    print("Reversed:", rev)

reverse_number()


## Check Palindrome Number

def palindrome_number():
    
    n = int(input())
    temp = n
    rev = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome_number()


## Q12. Weather Advisor (Real Scenario)

def weather_advisor():
    
    temp = float(input("Temperature: "))
    rain = input("Is it raining (yes/no): ")

    if temp > 35:
        if rain == "yes":
            print("Humid and hot - stay inside")
        else:
            print("Very hot - drink water")
    else:
        if rain == "yes":
            print("Carry umbrella")
        else:
            print("Weather is fine")

weather_advisor()


## Q13. Find First Even Number

def first_even():
    
    nums = list(map(int, input().split()))

    for n in nums:
        if n % 2 == 0:
            print("First even:", n)
            break
    else:
        print("No even number found")

first_even()


## Error Log Counter (DevOps Real)

def count_errors():
    
    logs = input("Enter logs: ").split()
    count = 0

    for log in logs:
        if log == "ERROR":
            count += 1

    print("Error count:", count)

count_errors()


## Numbers Divisible by 3 and 5 in Range

def divisible_range():
    
    start = int(input("Start: "))
    end = int(input("End: "))

    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

divisible_range()
