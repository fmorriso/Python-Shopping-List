'''
Answer may vary, but students are required to use the following:
1. A pantry list
2. User input into an ingredient list
3. Pass the ingredient list to a method
4. Use a conditional and loop in the method
'''

pantry = ["bread", "peanut butter", "pretzels", "chips"]


def display_shopping_list(missing_items):
    if len(missing_items) > 0:
        print("You need to go shopping!")
        print("The following ingredients are missing:")
        for item in missing_items:
            print(item)
    else:
        print("It looks like you have everything to make your recipe!")


def get_ingredients() -> list[str]:
    # ask the user for the items in what they want to eat
    recipe = []
    while True:
        ingredient = input("Please enter an ingredient ('done' when complete): ")
        if ingredient.lower() == "done":
            break
        recipe.append(ingredient)

    return recipe


def get_shopping_list(menu: list[str]) -> list[str]:
    shopping_needs = []
    for item in menu:
        if item.lower() not in pantry:
            shopping_needs.append(item)

    return shopping_needs


def main():
    # ask the user for the items in what they want to eat
    recipe = get_ingredients()

    # check the list of items in the recipe against what is in the pantry and show what is missing.
    shopping_list = get_shopping_list(recipe)

    # show what we need to go shopping for, if anything
    display_shopping_list(shopping_list)


if __name__ == '__main__':
    print(pantry)
    main()
