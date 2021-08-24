flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
    # 42,  # Join can't join ints to strings
]

# for flower in flowers:
#     print(flower)

# separator = ", "
separator = " | "
output = separator.join(flowers)
print(output)

print(", ".join(flowers))
