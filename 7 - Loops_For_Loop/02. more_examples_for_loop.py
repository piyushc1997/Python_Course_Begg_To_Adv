## Real DevOps Examples :-

# Example 1: Looping through a list of servers and performing an action on each server

servers = ["server1", "server2", "server3"]

for server in servers:
    print("Checking:", server)
    # Here you can add code to perform actions on each server, such as checking status, deploying updates, etc.


# Example 2: Looping through a list of log files and processing each file

log_files = ["log1.txt", "log2.txt", "log3.txt"]

for log_file in log_files:
    print("Processing log file:", log_file)
    # Here you can add code to read and process each log file, such as extracting information, analyzing data, etc.
    
    
# Example 3: Looping through a list of services and checking their status

services = ["nginx", "mysql", "redis"]

for service in services:
    print("Checking status of service:", service)
    # Here you can add code to check the status of each service, such as using system commands or APIs to get the status information.
    
    
# Example 4: Looping through a list of users and sending notifications

users = ["user1", "user2", "user3"]

for user in users:
    print("Sending notification to:", user)
    # Here you can add code to send notifications to each user, such as using email or messaging APIs to deliver the notifications.
    
    
# Example 5 : Restart multiple services

services = ["nginx", "mysql", "redis"]

for service in services:
    print("Restarting service:", service)
    # Here you can add code to restart each service, such as using system commands or APIs to perform the restart action.


# Example 6: Looping through a list of IP addresses and pinging each address

ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for ip in ip_addresses:
    print("Pinging IP address:", ip)
    # Here you can add code to ping each IP address, such as using system commands or libraries to perform the ping operation and check connectivity.   
    
    
# Example 7: Looping through a list of Docker containers and checking their status


containers = ["container1", "container2", "container3"]

for container in containers:
    
    print("Checking status of container:", container)
    # Here you can add code to check the status of each Docker container, such as using Docker commands or APIs to get the status information.  
    
    
# Example 8: Looping through a list of Kubernetes pods and checking their status

pods = ["pod1", "pod2", "pod3"]

for pod in pods:
    print("Checking status of pod:", pod)
    # Here you can add code to check the status of each Kubernetes pod, such as using kubectl commands or APIs to get the status information.


## Real AI/Data Examples :-

# Example 1: Looping through a list of numbers and calculating their squares

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    square = num ** 2
    print(f"The square of {num} is {square}")
    
    
# Example 2: Looping through a list of words and counting the number of characters in each word

words = ["hello", "world", "python"]

for word in words:
    length = len(word)
    print(f"The word '{word}' has {length} characters")
    
    
# Example 3: Looping through a list of data points and calculating their mean

data_points = [10, 20, 30, 40, 50]

total = 0

for point in data_points:
    
    total += point
    
mean = total / len(data_points)

print(f"The mean of the data points is {mean}")


# Example 4: Looping through a list of numbers and filtering out the even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers:", even_numbers)    


# Example 5: Looping through a list of sentences and counting the number of words in each sentence

sentences = ["Hello world", "Python is great", "I love programming"]

for sentence in sentences:
    word_count = len(sentence.split())
    print(f"The sentence '{sentence}' has {word_count} words")


# Example 6: Sum of numbers

total = 0

numbers = [10, 20, 30, 40]

for num in numbers:
    total += num

print("Total:", total)


total = 0

for i in range(1, 6):
    total = total + i

print(total)


# Example 7: Multiplication table 

number = 5

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
