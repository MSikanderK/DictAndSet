available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
cart = {}

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in cart:
            print(f"Removing {chosen_part}")
            cart.pop(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            cart[current_choice] = chosen_part
        print(f"Your cart now contains: {cart} ")
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
