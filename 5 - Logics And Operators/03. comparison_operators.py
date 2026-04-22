"""

What are Comparison Operators?

They compare two values and give: True or False


This is how Boolean values are created

"""

## Basic Examples :-

print(5 == 5)   # True

print(5 != 3)   # True

print(10 > 5)   # True

print(2 < 5)    # True

print(2 >= 5)   # True

print(5 >= 5)   # True

print(4 <= 5)   # True

print(3 < 1)    # False


## Real-World Examples :-

# Age Check

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
    

# Login Check

password = input("Enter password: ")

if password == "admin123":
    print("Login successful")
else:
    print("Wrong password")
    
    
# Pricee Comparison

price = 500

if price > 1000:
    print("Expensive")
else:
    print("Affordable")
    
    
# Practice :-

print(10 >= 10)
print(7 != 7)
print(3 < 5)
print("a" == "b")
print("a" < "b")
print("a" > "b")
