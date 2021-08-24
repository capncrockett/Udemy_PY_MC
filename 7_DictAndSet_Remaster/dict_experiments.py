from contents import recipes

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)

if a == b == c == d == e == f:
    print("Truthy")
else:
    print("Too bad")

print(len(b))           # 3
print(list(b))          # ['one', 'two', 'three']
print(b.items())        # dict_items([('one', 1), ('two', 2), ('three', 3)])
print(d.get('one'))     # 1

print()

dict_og = {'one': 1, 'two': 2, 'three': 3}

dict_copy = {}
dict_copy.update(dict_og)
dict_copy.update(recipes)

print(id(dict_og), dict_og)
print(id(dict_copy), dict_copy)
