from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index+1)] = key


shopping_cart = {}

while True:
    #menu of recipies
    print("Please Choose Your Recipie")
    print("--------------------------")
    for key,value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients....")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}.")
                add_shopping_item(shopping_cart, food_item, quantity_to_buy)
print("\tSHOPPING LIST")
for things in shopping_cart.items():
    print(things)
