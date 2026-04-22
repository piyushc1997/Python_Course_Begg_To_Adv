"""

Why Random is Important?

Used in real-world:

OTP generation
Games
Passwords
Simulations
Testing 

1. `random()`: This function returns a random float number between 0.0 and 1.0. For example: `random.random()` might return `0.37444887175646646`.
2. `randint(a, b)`: This function returns a random integer N such that  a <= N <= b. For example: `random.randint(1, 10)` might return `7`.
3. `choice(seq)`: This function returns a random element from the non-empty sequence seq. For example: `random.choice(['apple', 'banana', 'cherry'])` might return `'banana'`.
4. `shuffle(seq)`: This function shuffles the sequence seq in place. For example: `random.shuffle([1, 2, 3, 4, 5])` might change the list to `[3, 1, 5, 2, 4]`. 
5. `sample(population, k)`: This function returns a list of k unique elements chosen from the population sequence or set. For example: `random.sample([1, 2, 3, 4, 5], 3)` might return `[2, 4, 5]`.    


"""

# Importing the random module to use any random function

import random


# Example 01 :- random.randint() → Random Integer

print(f"The random number from 1 to 10 is : " , random.randint(1 , 10))


# Example 02 :- random.random() → Float and random.uniform()

print(f"The random number from 1 to 10 is: {random.random()}")

print(f"The random number from 1 to 10 is: {random.uniform(1.0, 10.0)}")


# Example 03 :- random.shuffle() → Shuffle List

cards = [1, 2, 3, 4, 5]

random.shuffle(cards)

print(cards)


## Real-World Mini Projects :-

# Project 01: OTP Generator

otp = random.randint(1000, 9999)

print(f"Your OTP is: {otp}")


# Project 02: Dice Game

dice = random.randint(1, 6)

print(f"You rolled: {dice}")


# Project 03: Random Winning Picker

users = ["Piyush", "Rahul", "Amit"]

winner = random.choice(users)

print(f"Winner is: {winner}")


# Project 04: Passsword Generator

chars = "abcdefghijklmnopqrstuvwxyz123456789"

password = ""

for i in range(6):
    password += random.choice(chars)

print(password)
