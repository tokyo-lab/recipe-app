import os
from pathlib import Path

category_path = Path("recipes")


def count_recipes(path):
    counter = 0

    for txt in Path(path).glob("**/*.txt"):
        counter += 1
    return counter


def clear_screen():
    # Clear the screen, platform independent
    os.system("cls" if os.name == "nt" else "clear")


def start():
    clear_screen()
    print("*" * 50)
    print("*" * 5 + " Welcome to recipe admin " + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"The recipes are in {category_path}")
    print(f"Total recipes: {count_recipes(category_path)}")

    menu_choice = "x"
    while not menu_choice.isnumeric() or int(menu_choice) not in range(1, 7):
        print("Choose an option: ")
        print(
            """
[1] - Read Recipe
[2] - Create New Recipe
[3] - Create New Category
[4] - Delete Recipe
[5] - Delete Category
[6] - End Program
              """
        )
        menu_choice = input()

    return int(menu_choice)


def return_begining():
    return_choice = "x"

    while return_choice.lower() != "b":
        return_choice = input("\nPress 'b' to return home")
