for i in range(10, 16):
    print("i is now {}".format(i))

print("-" * 30)

for i in range(0, 10):
    print("i is now {}".format(i))

print("-" * 30)

for i in range(10):
    print(i)

print("-" * 30)

for i in range(0, 10, 2):
    print("i is now {}".format(i))

print("-" * 30)

for i in range(10, 0, -2):
    print("i is now {}".format(i))

print("-" * 30)

# Solution 1
for i in range(0, 100, 7):
    print(i)

print("-" * 30)

# Solution 2
for i in range(101)[::7]:
    print(i)

print("-" * 30)

# Not a solution.
# for i in range(100, -0, -7):    # Doesn't show 0.
#     print(i)
#
