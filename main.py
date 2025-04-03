'''
Answer may vary, but students are required to use the following:
1. A pantry list
2. User input into an ingredient list
3. Pass the ingredient list to a method
4. Use a conditional and loop in the method
'''

pantry = ["bread", "peanut butter", "pretzels", "chips"]


def get_ingredients() -> list[str]:
    """
    Get a list of ingredients that the user wants to use to prepare a meal.
    :return: a list of ingredients needed to prepare the meal
    """
    recipe = []
    while True:
        ingredient = input("Please enter an ingredient ('done' when complete): ")
        if ingredient.lower() == "done":
            break
        recipe.append(ingredient)

    return recipe


def get_shopping_list(menu: list[str]) -> list[str]:
    """
    Using the supplied menu, check it against the pantry list to see which items are
    not in the pantry and need to be added to a shopping list.
    :param menu:
    :return:
    """
    shopping_needs = []
    for item in menu:
        if item.lower() not in pantry:
            shopping_needs.append(item)

    return shopping_needs


def display_shopping_list(missing_items: list[str]) -> None:
    """
    Display the shopping list or, if the shopping list is empty, display a message that
    informs the user that everything needed to prepare the meal is available already in the pantry.
    :param missing_items: the list of missing ingredients or an empty list.
    """
    if len(missing_items) > 0:
        print("You need to go shopping!")
        print("The following ingredients are missing:")
        for item in missing_items:
            print(item)
    elif len(missing_items) == 0:
        print('You did not enter any ingredients.')
    else:
        print("It looks like you have everything to make your recipe!")


def main():
    # ask the user for the items in what they want to eat
    recipe = get_ingredients()

    # check the list of items in the recipe against what is in the pantry and show what is missing.
    shopping_list = get_shopping_list(recipe)

    # show what we need to go shopping for, if anything
    display_shopping_list(shopping_list)


if __name__ == '__main__':
    print(f'here is what is already in the pantry: {pantry}')
    main()
