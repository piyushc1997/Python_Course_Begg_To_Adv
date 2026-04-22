## Logic Buildings :-

# Print Find largest number

numbers = [10, 20, 5, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)


# Print smallest number

numbers = [10, 20, 5, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)


# Print count of numbers > 10

numbers = [5, 12, 8, 20, 3]

count = 0

for num in numbers:
    if num > 10:
        count += 1
print("Count of numbers greater than 10:", count)


# Print product of all numbers

numbers = [2, 3, 4]

product = 1

for num in numbers:
    product *= num
print("Product of numbers:", product)


# Print factorial of a number

factorial = 1

for i in range(1, 7):
    factorial *= i
print(f"Factorial of 6 is {factorial}")


n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)


# Check if a number is prime or not

number = 17
is_prime = True

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
