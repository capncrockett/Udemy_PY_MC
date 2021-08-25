from contents import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key


def shopping_list(ingredients, pantry):
    """
    Add items to a shopping list.

    The function adds required items and their needed quantities to a
    shopping list.

    :param ingredients:
    :param pantry:
    :return: shopping list
    """
    shopping_list = {}  # Empty dict

    for food_item, required_quantity in ingredients.items():
        quantity_in_pantry = pantry.get(food_item, 0)
        if required_quantity <= quantity_in_pantry:
            print(f"\t{food_item}: Check")
        else:
            quantity_to_buy = required_quantity - quantity_in_pantry
            print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
            shopping_list[food_item] = quantity_to_buy

    return shopping_list

# shopping_list = {}


while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        print(f"Your shopping list {shopping_list(ingredients, pantry)}")

        # for food_item, required_quantity in ingredients.items():
        #     quantity_in_pantry = pantry.get(food_item, 0)
        #     if required_quantity <= quantity_in_pantry:
        #         print(f"\t{food_item}: Check")
        #     else:
        #         quantity_to_buy = required_quantity - quantity_in_pantry
        #         print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
        #         shopping_list[food_item] = quantity_to_buy
        #
        # print(f"Your shopping list: {shopping_list}")
