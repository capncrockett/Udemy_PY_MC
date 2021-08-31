from contents import pantry, recipes

# print(f"Recipes >>> {recipes}")
# print()
# print(f"Pantry >>> {pantry}")
# print()

display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_recipes = {}
for index, key in enumerate(recipes):
    # print(index, key)
    display_recipes[str(index + 1)] = key


# print(f" Display Recipes as Dict >>> {display_recipes}")
# print()


def add_shopping_item(shop_list: dict, item: str, quantity: int) -> None:
    """Add a tuple containing `item` and `quantity` to the `shop_list` dict"""
    # if item in shop_list:
    #     shop_list[item] += quantity
    # else:
    #     shop_list[item] = quantity
    shop_list[item] = shop_list.setdefault(item, 0) + quantity


# Empty shopping list
shopping_dict = {}

while True:
    # Display a menu of the recipes we know how to cook.
    print("Please choose your recipe")
    print("_________________________")

    for key, value in display_recipes.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_recipes:
        selected_item = display_recipes[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)

        # Iterate over ingredients in the chosen recipe.
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item}: OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_dict, food_item, quantity_to_buy)

for things in shopping_dict.items():
    print(things)
# print(shopping_dict)
# display_pantry = {}
# for index, key in enumerate(pantry):
#     display_pantry[str(index + 1)] = key

# for k, v in display_pantry.items():
#     print(f"{k} - {v}")
