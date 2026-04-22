## INTERVIEW CORE LEVEL PART 01:-

# FACTORIAL (VERY IMPORTANT)

n = 10
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)


# PRIME NUMBERS (VERY IMPORTANT)

num = 29    
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# FIBONACCI SEQUENCE (VERY IMPORTANT)

a = 0
b = 1

for i in range(5):
    print(a)
    a, b = b, a + b


# SUM OF DIGITS (IMPORTANT)

number = 12345
total = 0

for digit in str(number):
    total += int(digit)

print(f"The sum of the digits in {number} is {total}")


# Count Digits in a Number (IMPORTANT)

number = 12345
count = 0

for digit in str(number):
    count += 1

print(f"The number of digits in {number} is {count}")


# Reverse a Number (VERY IMPORTANT)

number = 12345
reverse = 0

for digit in str(number):
    reverse = digit + str(reverse)

print(f"The reverse of {number} is {reverse}")

    
# Check if a Number is an Palindrome (VERY IMPORTANT)

number = 12321
reverse = 0

for digit in str(number):
    reverse = digit + str(reverse)

if str(number) == reverse:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
    
    
# Check if a String is a Palindrome (VERY IMPORTANT)

string = "madam"
reverse = ""

for char in string:
    reverse = char + reverse
    
if string == reverse:
    print(f"{string} is a palindrome")  
else:
    print(f"{string} is not a palindrome")  
    
    
# Find Maximum Number and Minimum Number in a List (VERY IMPORTANT)

nums = [10, 5, 20, 3]

max_num = nums[0]
min_num = nums[0]

for n in nums:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print(max_num, min_num)


# Find Second Largest Number in a List (VERY IMPORTANT)

numbers = [10, 20, 5, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
second_largest = float('-inf')

for num in numbers:
    if num > second_largest and num < largest:
        second_largest = num

print("Second largest number:", second_largest)


# Count Even and Odd Numbers in a List (VERY IMPORTANT)

numbers = [1, 2, 3, 4, 5, 6]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1 
odd_count = len(numbers) - even_count

print("Even count:", even_count)
print("Odd count:", odd_count)
