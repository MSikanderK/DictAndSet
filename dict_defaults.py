from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

ketchup_quan = pantry.get("ketchup", 0)
print(f"ketchup : {ketchup_quan}")

z_quan = pantry.setdefault("zuccini", 8)
print(f"zucchini: {z_quan}")
print()

print("pantry now contains....")
for key, value in sorted(pantry.items()):
    print(key, value)