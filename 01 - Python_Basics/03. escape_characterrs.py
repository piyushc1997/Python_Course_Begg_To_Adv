"""
Escape characters are used to represent special characters inside a string.
They start with a backslash \ followed by a character that has a special meaning.

---------------------------------------------

Why Do We Need Escape Characters?

Because sometimes:

You want a new line
You want tab space
You want to use quotes inside quotes

--------------------------------------------


"""

# Most Important Escape Characters :-

# (A) New Line \n -> Moves text to the next line

print("Hello\nWorld")  # Output: Hello
                       #         World

print("Name: Piyush\nAge: 25\nCity: Kolkata") # Output: Name: Piyush
                                              #         Age: 25
                                              #         City: Kolkata

                      
# (B) Tab \t  -> Adds a tab space

print("Hello\tWorld")  # Output: Hello   World

print("Name:\tPiyush")
print("Age:\t25")
print("City:\tKolkata") # Output: Name:   Piyush
                        #         Age:    25
                        #         City:   Kolkata
                        
# (C) Backslash \\ -> To print a backslash

print("This is a backslash: \\")  # Output: This is a backslash: \
    
# (D) Single Quote \' -> To print a single quote

print('It\'s raining')  # Output: It's raining

# (E) Double Quote \" -> To print a double quote

print("She said, \"Hello!\"")  # Output: She said, "Hello!"

# (F) Carriage Return \r -> Moves the cursor to the beginning of the line

print("Hello\rWorld")  # Output: World -> Hello is overwritten by World

# (G) Backspace \b -> Deletes the previous character

print("Hello\bWorld")  # Output: HellWorld -> o is deleted by \b

# (H) Form Feed \f -> Moves the cursor to the next page (not commonly used)

print("Hello\fWorld")  # Output: Hello
                       #         World (on a new page, may not be visible in all environments)
                       
# (I) Unicode \u -> To print a Unicode character

print("\u03A9")  # Output: Ω (Greek capital letter Omega)

# (J) Raw String r (Very Important) -> To treat backslashes as literal characters

print(r"C:\Users\Piyush")  # Output: C:\Users\Piyush (backslashes are treated as literal characters)
