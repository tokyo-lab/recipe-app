import os
from pathlib import Path


category_path = Path("recipes")


def show_categories(category_path):
    print("Categories:")
    categories_list = []
    counter = 1

    for folder in category_path.iterdir():
        folder_str = str(folder.name)
        print(f"[{counter}] - {folder_str}")
        categories_list.append(folder)
        counter += 1

    return categories_list


def select_category(cat_list):
    correct_choice = "x"
    while not correct_choice.isnumeric() or int(correct_choice) not in range(
        1, len(cat_list) + 1
    ):
        correct_choice = input("\nChoose a categrory: ")

    return cat_list[int(correct_choice) - 1]


def create_category(category_path):
    exists = False

    while not exists:
        print("Write the name of the new category: ")
        category_name = input()
        new_path = Path(category_path, category_name)

        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f"Your category {category_name} has been created. ")
            exists = True
        else:
            print("That category already exists")


def delete_category(category):
    Path(category).rmdir()
    print(f"The category {category.name} has been removed")
