"""

LEVEL 1 (FORMULA-BASED CODING PROBLEMS)


"""

## 1. Simple Interest -> Formula: SI = (P × R × T) / 100

# Without def

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

print("Simple Interest:", si)

# With def

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input())
r = float(input())
t = float(input())

print(simple_interest(p, r, t))


## 2. Compound Interest -> Formula: CI = P(1 + R/100)^T − P

# Without def

p = float(input())
r = float(input())
t = float(input())

ci = p * (1 + r/100) ** t - p

print("CI:", ci)

# With def
def compound_interest(p, r, t):
    return p * (1 + r/100) ** t - p

p = float(input())
r = float(input())
t = float(input())

print(compound_interest(p, r, t))


## 3. Area of Circle -> πr²

# Without def

r = float(input())

area = 3.14 * r * r

print(area)

# With def

def area_circle(r):
    return 3.14 * r * r

print(area_circle(float(input())))


## 4. Area of Rectangle -> lenghth x breadth

# Without def

l = int(input())
b = int(input())

area = l * b

print(area)

# With def

def area_rect(l, b):
    return l * b

print(area_rect(int(input()), int(input())))


## 5. Area of Triangle -> ½ × base × height

# Without def

b = int(input())
h = int(input())

area = 0.5 * b * h

print(area)

# With def

def area_triangle(b, h):
    return 0.5 * b * h

print(area_triangle(int(input()), int(input())))


## 6. Perimeter of Rectangle -> 2(l + b)

# Without def

l = int(input())
b = int(input())

per = 2 * (l + b)

print(per)

# With def

def perimeter(l, b):
    return 2 * (l + b)

print(perimeter(int(input()), int(input())))


## 7. Celsius to Fahrenheit -> (C × 9/5) + 32

# Without def

c = float(input())
f = (c * 9/5) + 32

print(f)

# With def

def c_to_f(c):
    return (c * 9/5) + 32

print(c_to_f(float(input())))


## 8. Kilometer to Meter -> 1 km = 1000 m

# Without def

km = float(input())
m = km * 1000

print(m)

# With def

def km_to_m(km):
    return km * 1000

print(km_to_m(float(input())))


## Calculate Power -> a^b

# Without def

a = int(input())
b = int(input())

print(a ** b)

# With def

def power(a, b):
    return a ** b

print(power(int(input()), int(input())))


## Speed Calculation -> speed = distance / time

# Without def

d = float(input())
t = float(input())

speed = d / t

print(speed)

# With def

def speed(d, t):
    return d / t

print(speed(float(input()), float(input())))
