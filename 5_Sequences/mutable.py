shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

# lists are mutable. We were able to add an item
# and the address remained the same.

print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)
print(e)
print("Adding sugar")
c.append("sugar")
print(f)
