"""

What is a Nested Loop?

A loop inside another loop. 

The "inner loop" will be executed one time for each iteration of the "outer loop".

-----------------------------------------


Example:

for i in range(1, 4): # Outer loop
    for j in range(1, 4): # Inner loop
        print(i, j)
        
Output:
1 1  1 2  1 3
2 1  2 2  2 3
3 1  3 2  3 3

-----------------------------------------

Outer loop → controls rows
Inner loop → controls columns

-----------------------------------------

IMPORTANT RULE (REMEMBER)

Pattern =

Outer loop → rows
Inner loop → what to print

"""

## Level 1 - Basic Patterns :-

# Pattern 1 - Square Pattern

n = 4

for i in range(n): # Outer loop
    for j in range(n): # Inner loop
        print("*", end=" ") # end=" " is used to print in the same line
    print() # This will print a new line after each row
    
    
# Pattern 2 - Right Angled Triangle

n = 4

for i in range(1, n+1): # Outer loop
    for j in range(1, i+1): # Inner loop
        print("*", end=" ") # end=" " is used to print in the same line
    print() # This will print a new line after each row
    
    
# Number Triangle 

n = 4

for i in range(1, n+1): # Outer loop
    for j in range(1, i+1): # Inner loop
        print(j, end=" ") # end=" " is used to print in the same line
    print() # This will print a new line after each row



## LEVEl 2 - REVERSE Patterns :-

# Pattern 1 - Reverse Triangle 

n = 4

for i in range(n, 0, -1): # Outer loop
    for j in range(1, i+1): # Inner loop
        print("*", end=" ") # end=" " is used to print in the same line
    print() # This will print a new line after each row


# Reverse Number Triangle 

n = 4

for i in range(n, 0, -1): # Outer loop
    for j in range(1, i+1): # Inner loop
        print(j, end=" ") # end=" " is used to print in the same line
    print() # This will print a new line after each row
    
    
## LEVEL 3: PYRAMID PATTERNS

# Pyramid Pattern

n = 4

for i in range(1, n+1): # Outer loop
    # Print spaces
    for j in range(n-i):
        print(" ", end=" ")
    # Print stars
    for k in range(2*i-1):
        print("*", end=" ")
    print() # This will print a new line after each row
    
# Method 2 - Pyramid Pattern

for i in range(1, 5):
    for space in range(4 - i):
        print(" ", end="")

    for star in range(i):
        print("* ", end="")

    print()
    

# Reverse Pyramid Pattern

n = 4

for i in range(n, 0, -1): # Outer loop
    # Print spaces
    for j in range(n-i):
        print(" ", end=" ")
    # Print stars
    for k in range(2*i-1):
        print("*", end=" ")
    print() # This will print a new line after each row
    
# Method 2 - Reverse Pyramid Pattern

for i in range(4, 0, -1):
    for space in range(4 - i):
        print(" ", end="")

    for star in range(i):
        print("* ", end="")

    print()
