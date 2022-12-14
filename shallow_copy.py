import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# perform a shallow copy
# things = animals.copy()

# deep copy
things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])

print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(id(things["teddy"]), things["teddy"])

print(id(animals["teddy"]), animals["teddy"])
