from contents import recipes

def deep_copy(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict

recipes_copy = deep_copy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])