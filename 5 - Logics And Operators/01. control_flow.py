"""

Control Flow means:

In what order your code runs


"""

## Types of Control Flow :-

# There are only 3 types:

# Sequential (Normal flow) -> Code runs line by line

print("Step 1")
print("Step 2")
print("Step 3")


# Conditional (Decision flow)

age = 20

if age >= 18:
    print("Adult")
    
    
# Looping (Repeat flow)  -> Repeat code multiple times -> (For Loop, While Lopp etc)


# Real-Life Example (Very Important):

signal = "green"

if signal == "green":
    print("Go")
    
# This is control flow changing based on condition


## Real-World Examples :-

# ATM Withdrawal

balance = 1000
withdraw = 500

if withdraw <= balance:
    print("Transaction successful")
