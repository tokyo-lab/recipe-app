from pathlib import Path
import os


def clear_screen():
    # Clear the screen, platform independent
    os.system("cls" if os.name == "nt" else "clear")


def get_category():
    category_path = Path("categories")
    user_choice = ""
    # List directories using glob
    # Enumerate and list directories, creating a dictionary with indices
    category_dict = {
        index: category.name
        for index, category in enumerate(category_path.iterdir())
        if category.is_dir()
    }
    # Print category options
    for index, category in category_dict.items():
        print(f"[{index + 1}] - {category}")

    # Get user input
    try:
        user_choice = int(input("Select a category: ")) - 1
        if user_choice in category_dict:
            clear_screen()
            print(f"You selected {category_dict[user_choice]}")
        else:
            print("Invalid selection. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return user_choice


def create_category():
    while True:
        category = input("Enter a category to create: ")
        folder = Path("categories") / category

        if folder.exists():
            clear_screen()
            print(f"The category '{folder} already exist")
            break
        else:
            # Create the folder
            folder.mkdir(parents=True, exist_ok=True)
            clear_screen()
            print(f"The folder '{folder}' has been created.")
            break


def delete_category():
    while True:
        category = input("Enter a category to delete: ")
        folder = Path("categories") / category
        if folder.exists():
            folder.rmdir()
            clear_screen()
            print(f"The category '{folder}' has been deleted.")
            break
        else:
            clear_screen()
            print(f"The category '{folder} does not exist")


def create_recipe(category):
    while True:
        recipe = input(f"Enter a recipe to create in the {category} category: ")
        folder = Path("categories") / category
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


def get_recipe(category):
    category_path = Path("categories") / category
    user_choice = ""

    # Check if category exist
    if not category_path.exists() or not category_path.is_dir():
        print(f"No such category: {category}")
        return

    # List directories using glob
    # Enumerate and list directories, creating a dictionary with indices
    recipe_dict = {
        index: recipe.stem  # Use stem to get the filename without the extension
        for index, recipe in enumerate(category_path.iterdir())
        if recipe.is_file()
    }
    # Print recipe options
    for index, recipe in recipe_dict.items():
        print(f"[{index + 1}] - {recipe}")

    # Get user input
    while True:
        try:
            user_choice = int(input("Select a recipe: ")) - 1
            if user_choice in recipe_dict:
                clear_screen()
                print(f"You selected {recipe_dict[user_choice]}")
                break
            else:
                print("Invalid selection. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return user_choice


def delete_recipe(category):
    while True:
        recipe = input("Enter a recipe to delete: ")
        folder = Path("categories") / category
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


# get_category()
# create_recipe("Pasta")
# get_recipe("Pasta")
delete_recipe("Pasta")
