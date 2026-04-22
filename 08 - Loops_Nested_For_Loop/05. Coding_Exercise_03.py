## LEVEL 2: NUMBER PATTERNS

# Pattern 1 - Square Pattern

n = 3

for i in range(n): # Outer loop
    for j in range(n): # Inner loop
        print(j+1, end = " ") # end=" " is used to print in the same line
    print() # This will print a new line after each row
    
    
# Increasig Number Triangle

n = 3

for i in range(n): # Outer loop
    for j in range(i+1): # Inner loop
        print(j+1, end = " ") # end=" " is used to print in the same line
    print() # This will print a new line after each row
    
    
# Continuous Number Triangle (Important)

n = 3

num = 1 # This variable will keep track of the current number to print

for i in range(n): # Outer loop
    for j in range(i+1): # Inner loop
        print(num, end = " ") # end=" " is used to print in the same line
        num += 1 # Increment the number for the next print
    print() # This will print a new line after each row
