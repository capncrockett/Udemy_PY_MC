# import json
from operator import add
# import requests
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# print(response)
# print(todos)
#
# todos = response.json()
# print(type(todos))
#
# print(todos[:10])


from functools import reduce


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


# my_add(5, 5)

numbers = [0, 1, 2, 3, 4]

reduce(my_add, numbers)
reduce(my_add, numbers, 100)

total = 0
for num in numbers:
    total += num
print(total)

print(reduce(lambda a, b: a + b, numbers))

print(add(1, 2))
print(reduce(add, numbers))

print(sum(numbers))


