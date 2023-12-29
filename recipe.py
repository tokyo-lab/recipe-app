import os
from pathlib import Path


def show_recipes(category_path):
    print("These are the recipes:")
    recipes_path = Path(category_path)
    recipes_list = []
    counter = 1

    for recipe in recipes_path.glob("*.txt"):
        recipe_str = str(recipe.name)
        print(f"[{counter}] - {recipe_str}")
        recipes_list.append(recipe)
        counter += 1

    return recipes_list


def select_recipe(recipe_list):
    selected_recipe = "x"
    while not selected_recipe.isnumeric() or int(selected_recipe) not in range(
        1, len(recipe_list) + 1
    ):
        selected_recipe = input("\nChoose a recipe: ")

    return recipe_list[int(selected_recipe) - 1]


def read_recipe(recipe):
    print(Path.read_text(recipe))


def create_recipe(category):
    exists = False

    while not exists:
        print("Write the name of your recipe: ")
        recipe_name = input() + ".txt"
        print("Write your new recipe: ")
        recipe_content = input()
        new_path = Path(category, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)
            print(f"Your recipe {recipe_name} has been created. ")
            exists = True
        else:
            print("That recipe already exists")


def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f"The recipe {recipe.name} has been deleted")
