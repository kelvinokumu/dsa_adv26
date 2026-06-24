import random

def basic(n):

    if n == 0:
        return n

    basic(n-1)
    print(n)

num = random.randint(1, 10)
print(f"The number is {num}")
basic(num)