from pathlib import Path
from utilities import clear_screen


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
