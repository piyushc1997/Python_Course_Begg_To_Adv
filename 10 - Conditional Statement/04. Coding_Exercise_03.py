"""

LEVEL 3 — CONDITIONAL STATEMENTS (NESTED + REAL LOGIC)


"""

## Login System (Basic Authentication)

def login(user, pwd):
    
    if user == "admin":
        if pwd == "1234":
            print("Login Successful")
        else:
            print("Wrong Password")
    else:
        print("User Not Found")

login(input(), input())


## Q2. ATM Withdrawal System

def withdraw(balance, amount):
    
    if amount <= balance:
        if amount % 100 == 0:
            print("Success")
        else:
            print("Invalid Denomination")
    else:
        print("Insufficient Balance")

withdraw(10000, int(input()))


## Student Result with Distinction

def result(marks):
    
    if marks >= 40:
        if marks >= 75:
            print("Distinction")
        else:
            print("Pass")
    else:
        print("Fail")

result(int(input()))


## Triangle Valid + Type

def triangle(a, b, c):
    
    if a + b > c and b + c > a and a + c > b:
        if a == b and b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")

triangle(int(input()), int(input()), int(input()))


## Password Strength (Improved)

def check_pwd(pwd):
    
    if len(pwd) >= 8:
        if any(c.isdigit() for c in pwd):
            if any(c.isalpha() for c in pwd):
                print("Strong")
            else:
                print("Add letters")
        else:
            print("Add digits")
    else:
        print("Short")

check_pwd(input())


## Server Health Decision (DevOps Real Case)

cpu = 85
memory = 70

def server(cpu, memory):
    
    if cpu > 80:
        if memory > 65:
            print("Scale Up")
        else:
            print("Check Memory")
    else:
        if cpu < 30:
            print("Scale Down")
        else:
            print("Stable")

server(85, 70)


## Electricity Bill

def bill_calc(units):
    
    if units <= 100:
        bill = units * 5
    else:
        if units <= 200:
            bill = 100 * 5 + (units - 100) * 7
        else:
            bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print(bill)

bill_calc(int(input()))
