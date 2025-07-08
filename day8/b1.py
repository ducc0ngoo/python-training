import random

c = 0
guess_number = random.randint(1, 1000)
while True:
    n = int(input("Please guess the number: "))
    if n == guess_number:
        print("Correct!)#($*@)(")
        print(f"You guessed {c} times")
        break
    elif n > guess_number:
        print("The number is too high!")
    else:
        print("The number is too low!")
    c += 1
