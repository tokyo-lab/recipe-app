import os
from pathlib import Path
from utilities import clear_screen


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


def create_recipe(category_path):
    exists = False

    while not exists:
        print("Write the name of your recipe: ")
        recipe_name = input() + ".txt"
        print("Write your new recipe: ")
        recipe_content = input()
        new_path = Path(category_path, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)
            print(f"Your recipe {recipe_name} has been created. ")
            exists = True
        else:
            print("That recipe already exists")

    while True:
        recipe = input(f"Enter a recipe to create in the {category} category: ")
        folder = Path("recipes") / category
        file_name = recipe + ".txt"
        recipe_path = folder / file_name

        if recipe_path.exists():
            clear_screen()
            print(f"The recipe '{recipe}' already exist")
        else:
            # Create the recipe
            recipe_path.write_text(recipe)
            print(f"The recipe '{recipe}' has been created.")
            break


def delete_recipe(category, recipe):
    while True:
        folder = Path("recipes") / category
        file_name = recipe + ".txt"

        # create full file path
        file_path = folder / file_name

        if file_path.exists():
            file_path.unlink()
            clear_screen()
            print(f"The recipe '{recipe}' has been deleted.")
            break
        else:
            clear_screen()
            print(f"The recipe '{recipe} does not exist")

    result = get_recipe(category)

    if result is not None:
        selected_index, selected_recipe = result
        print(f"You selected index: {selected_index}, recipe name: {selected_recipe}")
    else:
        print("Recipe selection was not successful.")
