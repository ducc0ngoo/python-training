count = 0
for i in range(1, 101):
    if i % 15 == 0:
        print("Fizz Buzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
    count = count + 1
    if count % 15 == 0:
        print()
