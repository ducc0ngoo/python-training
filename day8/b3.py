for v in range(2, 101):
    for i in range(2, v):
        if v % i == 0:
            break
    else:
        print(f"{v} is a prime number!")
