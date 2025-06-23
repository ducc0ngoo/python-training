"""
int
float .
str
bool True/False
"""
# print(1/0)

# x = int(input())
# s = input()
# f = float(input())
# b = bool(input())
"""
output = "{nam} is {age} years old, and {name} works as a {job}."
print(output.format(name="John", job="web developer", age=24, nam=100))
"""
## - 1
greeting = "Hello, world"
print(greeting + "!")

print("{}!".format(greeting))

print(f"{greeting}!")

## - 2
name = input().strip().title()
print(f"Hello, {name}!")

## - 3
age = 29
print(f"I am {age}")

## - 4
title = "joker"
director = "todd Phillips"
release_year = 2019
print(f"{title.capitalize()} ({release_year}), directed by {director.title()}")
