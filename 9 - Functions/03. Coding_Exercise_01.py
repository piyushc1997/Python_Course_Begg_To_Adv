## Calculate the square of a number

# With def()

def square(n):
    return n * n

n = int(input("Enter a number: "))
print("Square:", square(n))

# Without def()

n = int(input("Enter a number: "))
result = n * n
print("Square:", result)


## Calculate the cube of a number

# With def()
def cube(n):
    return n * n * n

n = int(input("Enter a three numbers: "))
print("Cube:", cube(n))

result = cube(3)
print(result)  # Output: 27

# Without def()

n = int(input("Enter a number: "))
result = n * n * n

print("Cube:", result)


## Calculate the product of four numbers

# With def() 

def product(a, b, c, d):
    return a * b * c * d

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

print("Product:", product(a, b, c, d))

# Without def()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

result = a * b * c * d
print("Product:", result)


## Calculate Average of Five Numbers

# With def() 

def average(a, b, c, d, e):
    return (a + b + c + d + e) / 5

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))

print("Average:", average(a, b, c, d, e))

# Without def()

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))

avg = (a + b + c + d + e) / 5
print("Average:", avg)

## Calculate the Third Angle of a Triangle

# With def()

def third_angle(first, second):
    return 180 - (first + second)

first = int(input("Enter first angle: "))
second = int(input("Enter second angle: "))

print("Third angle:", third_angle(first, second))

# Without def()

first = int(input("Enter first angle: "))
second = int(input("Enter second angle: "))

third = 180 - (first + second)
print("Third angle:", third)    

## Calculate the Sum of Squares of First n Even Numbers

# With def()

def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        even = 2 * i
        total += even ** 2
    return total

n = int(input("Enter value of n: "))
print("Sum of squares:", sum_of_squares(n))

# Without def()

n = int(input("Enter value of n: "))

total = 0
for i in range(1, n + 1):
    even = 2 * i
    total += even ** 2

print("Sum of squares:", total)
