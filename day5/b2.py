numbers = [1, 2, 3, 4]
print(id(numbers))
new_numbers = numbers + [5]
print(id(new_numbers))

numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))
