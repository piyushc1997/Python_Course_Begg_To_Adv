## Pattern 1 - Square Pattern

n = 5

for i in range(n): # Outer loop
    for j in range(n): # Inner loop
        print("*", end = " ") # end=" " is used to print in the same line
    print() # This will print a new line after each row

n = 5

for i in range(n): # Outer loop
    for j in range(n+1): # Inner loop
        print(j+1, end = " ") # end=" " is used to print in the same line
    print() # This will print a new line after each row
