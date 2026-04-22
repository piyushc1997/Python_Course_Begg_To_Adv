# Pattern 2 - Right Angled Triangle

n = 5

for i in range(n): # Outer loop
    for j in range(i+1): # Inner loop
        print("*", end = " ") # end=" " is used to print in the same line
    print() # This will print a new line after each row


n = 5

for i in range(n): # Outer loop
    for j in range(i+1): # Inner loop
        print(i+1, end = " ") # end=" " is used to print in the same line
    print() # This will print a new line after each row
