"""
>, <, >=, <=, ==, != => True/False
not > and > or

first and second
bool(first) = True => second otherwise first

first or second
bool(first) = True => first otherwise second

if
elif
else
"""
name = input("Please enter your name: ")

if name:  # Checks the truth value of name by calling bool
      print(f"You entered {name}")
else:
      print("You didn't type anything")

