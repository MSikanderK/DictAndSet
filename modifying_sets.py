numbers = set()

# print(type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# unique_colours = sorted(set(data))
# print(unique_colours)

#keeping order
unique_colours  = list(dict.fromkeys(data))
print(unique_colours)
