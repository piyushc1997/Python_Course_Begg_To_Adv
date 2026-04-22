"""

Print Number of Minutes in a Day

Problem Statement :

You are required to write a Python program that calculates and prints the total number of minutes in a day.

There are 60 minutes in an hour and 24 hours in a day. Your task is to calculate the total number of minutes in a day by multiplying the number of minutes in an hour by the number of hours in a day. Your program should print the result.

Input Format :
There are no inputs for this task.

Output Format :
The output should be a single integer, the total number of minutes in a day (1440).


"""

total_mins_in_hour = 60
total_hours_in_day = 24

total_mins_in_day = total_mins_in_hour * total_hours_in_day
print(f"Total minutes in a day: {total_mins_in_day}")  # Output: 1440
