from pathlib import Path
from utilities import clear_screen


def get_category():
    category_path = Path("recipes")
    user_choice = ""
    # List directories using glob
    # Enumerate and list directories, creating a dictionary with indices
    sorted_categories = sorted(
        category.name for category in category_path.iterdir() if category.is_dir()
    )
    category_dict = {
        index: category for index, category in enumerate(sorted_categories)
    }
    # Print category options
    for index, category in category_dict.items():
        print(f"[{index + 1}] - {category}")

    # Get user input
    while True:
        try:
            user_choice = int(input("Select a category: ")) - 1
            if user_choice in category_dict:
                # clear_screen()
                return (user_choice, category_dict[user_choice])
            else:
                print("Invalid selection. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def create_category():
    while True:
        category = input("Enter a category to create: ")
        folder = Path("recipes") / category

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
        folder = Path("recipes") / category
        if folder.exists():
            folder.rmdir()
            clear_screen()
            print(f"The category '{folder}' has been deleted.")
            break
        else:
            clear_screen()
            print(f"The category '{folder} does not exist")
