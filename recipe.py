from pathlib import Path
from utilities import clear_screen


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
