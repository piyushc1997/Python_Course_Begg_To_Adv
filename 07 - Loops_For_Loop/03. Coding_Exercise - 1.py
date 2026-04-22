
# Print numbers from 1 to 10

for i in range(1, 11):
    print(i)
    
    
# Print Square of numbers

sum_of_squares = 0

for i in range(1, 11):
    sum_of_squares = sum_of_squares + i ** 2
    
print("Sum of squares:", sum_of_squares)


# Print Cube of numbers

sum_of_cubes = 0

for i in range(1, 11):
    sum_of_cubes = sum_of_cubes + i ** 3
print("Sum of cubes:", sum_of_cubes)


# Print Sum of numbers (1–10)

total = 0

for i in range(1, 11):
    total += i
print("Total:", total)


# Print Even numbers from 1 to 10

for i in range(1, 11):
    
    if i % 2 == 0:
        print(i)
        
        
# Print Odd numbers from 1 to 10

for i in range(1, 11):
    
    if i % 2 != 0:
        print(i)
