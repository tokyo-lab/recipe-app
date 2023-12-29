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


start()


def get_actions():
    actions_dict = {
        1: "Read Recipe",
        2: "Create Recipe",
        3: "Delete Recipe",
        4: "Create Category",
        5: "Delete Category",
        6: "End Program",
    }
    # Print action options
    for index, action in actions_dict.items():
        print(f"[{index}] - {action}")
    return actions_dict
