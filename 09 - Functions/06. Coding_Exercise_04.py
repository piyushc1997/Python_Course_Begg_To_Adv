"""

LEVEL 3 (LOGIC BUILDING)


"""

## Star Pattern (Right Triangle)

# With def

def pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()

n = int(input("Enter rows: "))
pattern(n)

# Without def

n = int(input("Enter rows: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
    

## Reverse Star Pattern

# With def

def reverse_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

n = int(input())
reverse_pattern(n)

# Without def

n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
    
    
## Sum of List Elements -> Example: [1,2,3] → 6

# With def

def sum_list(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

lst = list(map(int, input("Enter numbers: ").split()))

print(sum_list(lst))

# Without def

lst = list(map(int, input().split()))
total = 0

for num in lst:
    total = total + num

print(total)


## Find Maximum in List

# With def

def find_max(lst):
    max_val = lst[0]
    
    for num in lst:
        if num > max_val:
            max_val = num
    
    return max_val

lst = list(map(int, input().split()))

print(find_max(lst))

# Without def

lst = list(map(int, input().split()))
max_val = lst[0]

for num in lst:
    if num > max_val:
        max_val = num

print(max_val)


## Count Frequency of Elements -> Example: [1,2,1] → 1:2 times

# With def

def frequency(lst):
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count = count + 1
        print(i, ":", count)

lst = list(map(int, input().split()))

frequency(lst)

# Without def

lst = list(map(int, input().split()))

for i in lst:
    count = 0
    for j in lst:
        if i == j:
            count = count + 1
    print(i, ":", count)
    
    
## Remove Duplicates from List

# With def

def remove_duplicates(lst):
    new_list = []
    
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    
    return new_list

lst = list(map(int, input().split()))

print(remove_duplicates(lst))

# Without def

lst = list(map(int, input().split()))
new_list = []

for num in lst:
    if num not in new_list:
        new_list.append(num)

print(new_list)


## Reverse a String -> "abc" → "cba"

# With def

def reverse_string(s):
    rev = ""
    
    for i in s:
        rev = i + rev
    
    return rev

s = input("Enter string: ")

print(reverse_string(s))

# Without def

s = input()
rev = ""

for i in s:
    rev = i + rev

print(rev)


## Check Palindrome String -> "madam" → palindrome

# With def

def is_palindrome(s):
    rev = ""
    
    for i in s:
        rev = i + rev
    
    if s == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(is_palindrome(input()))

# Without def

s = input()
rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
## Count Vowels and Consonants -> Check each character

# With def

def count_vowels(s):
    vowels = 0
    consonants = 0
    
    for ch in s:
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    
    return vowels, consonants

s = input()
v, c = count_vowels(s)

print("Vowels:", v)
print("Consonants:", c)

# Without def

s = input()
vowels = 0
consonants = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
