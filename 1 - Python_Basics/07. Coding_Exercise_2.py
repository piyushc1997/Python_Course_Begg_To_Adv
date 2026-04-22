"""

Print Number of Seconds in a Day

Problem Statement :

You are required to write a Python program that calculates and prints the total number of seconds in a day.

There are 60 seconds in a minute, 60 minutes in an hour, and 24 hours in a day. Your task is to calculate the total number of seconds in a day by multiplying the number of seconds in a minute, the number of minutes in an hour, and the number of hours in a day. Your program should print the result.

Input Format :
There are no inputs for this task.

Output Format :
The output should be a single integer, the total number of seconds in a day (86400).


"""

total_secs_in_min = 60
total_mins_in_hour = 60 
total_hours_in_day = 24

total_secs_in_day = total_secs_in_min * total_mins_in_hour * total_hours_in_day

print(f"Total seconds in a day: {total_secs_in_day}")  # Output: 86400
