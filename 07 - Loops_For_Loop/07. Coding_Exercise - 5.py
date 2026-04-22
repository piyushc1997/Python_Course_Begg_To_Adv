## INTERVIEW CORE LEVEL PART 02:-

# Armstrong Number (VERY IMPORTANT)

num = 153
power = len(str(num))
total = 0

for digit in str(num):
    total += int(digit) ** power

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    
    
# Sum of Odd Digits (IMPORTANT)

number = 12345
total = 0

for digit in str(number):
    if int(digit) % 2 != 0:
        total += int(digit)
        
print(f"The sum of odd digits in {number} is {total}")


# Sum of Even Digits (IMPORTANT)

number = 12345
total = 0

for digit in str(number):
    if int(digit) % 2 == 0:
        total += int(digit)
        
print(f"The sum of even digits in {number} is {total}")


# FIND DUPLICATES IN LIST (VERY IMPORTANT)

numbers = [1, 2, 3, 4, 2, 5, 1]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate numbers:", duplicates)


# REMOVE DUPLICATES (VERY IMPORTANT)

numbers = [1, 2, 3, 4, 2, 5, 1]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        
print("Unique numbers:", unique_numbers)

nums = [1, 2, 2, 3, 1]
unique = list(set(nums))

print(unique)


# Sum of Digits in a Number (IMPORTANT)

number = 12345
total = 0

for digit in str(number):
    total += int(digit)
    
print(f"The sum of the digits in {number} is {total}")


# Count Frequency of Digits in a Number (IMPORTANT)

nums = [1, 2, 2, 3]

freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(f"Frequency of each digit in {nums}: {freq}")


# Find Missing Number in a List (VERY IMPORTANT)

numbers = [1, 2, 4, 5]
missing_number = None

for i in range(1, 6):
    if i not in numbers:
        missing_number = i
        break
print("Missing number:", missing_number)
