from pathlib import Path

category_path = "categories"


def choose_category(categories):
    category = input("Select a category")
    return category


def create_category():
    while True:
        category = input("Enter a category to create: ")
        folder = Path(category)
        if folder.exists():
            print("This category already exist")
        else:
            # Create the folder
            folder.mkdir(parents=True, exist_ok=True)
            print(f"The folder '{folder}' has been created.")


def delete_category():
    while True:
        category = input("Enter a category to delete: ")
        folder = Path(category)
        if folder.exists():
            folder.rmdir()
            print(f"The folder '{folder}' has been deleted.")

        else:
            print("This category does not exist")


delete_category()
