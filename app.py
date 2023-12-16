from utilities import get_actions
import category
import recipe


actions = get_actions()
# Print action options
for index, action in actions.items():
    print(f"[{index}] - {action}")

while True:
    try:
        user_choice = int(input("Select an action: "))
        if user_choice == 1:
            category = category.get_category()
            recipe.get_recipe(category)
        elif user_choice == 2:
            recipe.create_recipe()
        else:
            print("Invalid selection. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
