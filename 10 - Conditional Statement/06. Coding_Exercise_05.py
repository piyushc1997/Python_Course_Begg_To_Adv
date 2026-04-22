"""

LEVEL 5 — FUNCTIONS + REAL INTERVIEW PROBLEMS


"""

## Second Largest Number (Without Sorting)

def second_largest():
    
    nums = list(map(int, input("Enter numbers: ").split()))

    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n

    if second == float('-inf'):
        print("No second largest")
    else:
        print("Second largest:", second)

second_largest()


## Armstrong Number

def armstrong():
    
    n = int(input("Enter number: "))
    temp = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    if total == temp:
        print("Armstrong")
    else:
        print("Not Armstrong")

armstrong()


## 