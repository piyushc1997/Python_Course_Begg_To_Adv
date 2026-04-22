## String Based Examples :-

# Example 01 :- (Loop with a String)

name = "Hello"

for char in name:
    print(char)
    
    
# Example 02 :- (Loop with a String)

sentence = "Python is great"

for word in sentence.split():
    print(word)
    
    
# Example 03 :- (Loop with a String)

paragraph = "This is a sample paragraph. It contains multiple sentences. We will loop through it."

for sentence in paragraph.split('.'):
    print(sentence.strip())


# Example 04 :- (Loop with a String)

text = "Data Science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data."

for word in text.split():
    if word.lower() in ["data", "science"]:
        print(word)
        
        
# Example 05 :- Reverse a String

input_string = "Hello World"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_string}")


# Example 06 :- Counting Vowels in a String

input_string = "This is a sample string to count vowels."
vowel_count = 0

for char in input_string:
    if char.lower() in "aeiou":
        vowel_count += 1
        
print(f"Number of vowels in the string: {vowel_count}")
