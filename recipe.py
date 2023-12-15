from pathlib import Path

category_path = "categories"


def choose_category(categories):
    category = input("Select a category")
    return category


def create_category():
    while True:
        category = input("Enter a new category: ")
        folder = Path(category)
        if folder.exists():
            print("This category already exist")
        else:
            # Create the folder
            folder.mkdir(parents=True, exist_ok=True)
            print(f"The folder '{folder}' has been created.")


create_category()
