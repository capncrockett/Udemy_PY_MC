import random

for i in range(20):
    x = random.randint(-5, 5)
    if x == 0:
        continue
    print(1/float(x))
