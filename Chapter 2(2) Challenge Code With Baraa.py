import random

a = random.randint(1, 100)
a = a % 2

if a == 1:
    print("ODD Number")
elif a == 0:
    print("EVEN Number")
