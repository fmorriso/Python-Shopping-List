'''
Answer may vary, but students are required to use the following:
1. A pantry list
2. User input into an ingredient list
3. Pass the ingredient list to a method
4. Use a conditional and loop in the method
'''

pantry = ["bread", "peanut butter", "pretzels", "chips"]


def display_shopping_list(ingredients):
    shopping_list = []
    for item in ingredients:
        if item.lower() not in pantry:
            shopping_list.append(item)

    if len(shopping_list) > 0:
        print("You need to go shopping!")
        print("The following ingredients are missing:")
        for item in shopping_list:
            print(item)
    else:
        print("It looks like you have everything to make your recipe!")


def main():
    # ask the user for the items in what they want to eat
    recipe = []
    while True:
        ingredient = input("Please enter an ingredient ('done' when complete): ")
        if ingredient.lower() == "done":
            break
        recipe.append(ingredient)

    # check the list of items in the recipe against what is in the pantry and show what is missing.
    display_shopping_list(recipe)

if __name__ == '__main__':
    main()

