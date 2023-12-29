from utilities import get_actions
from pathlib import Path

import recipe_category
import recipe


def get_action_name():
    while True:
        actions_dict = get_actions()
        action_number = input("Select an action: ")

        try:
            action_number = int(action_number)
            action_name = actions_dict.get(action_number)
            if action_name is not None:
                return action_number, action_name
            else:
                print("Invalid selection. Select a valid number")
        except ValueError:
            print("Invalid input")


menu = 0
category_path = Path("recipes")
if menu == 1:
    all_categories = recipe_category.show_categories(category_path)
    selected_category = recipe_category.select_category(all_categories)


# while True:
#     selected_action_number, selected_action_name = get_action_name()
#     print("selected_action_number -> ", selected_action_number)
#     print("selected_action_name -> ", selected_action_name)

#     # View recipe
#     if selected_action_number == 1:
#         selected_category = recipe_category.get_category()
#         print("selected category -> ", selected_category)
#         recipe.get_recipe(selected_category)

#     # Create recipe
#     elif selected_action_number == 2:
#         selected_category = recipe_category.get_category()
#         print("selected category -> ", selected_category)
#         recipe.create_recipe(selected_category)

#     # Delete recipe
#     elif selected_action_number == 3:
#         print("Here are all the categories. Pick one: ")
#         selected_category = recipe_category.get_category()
#         print("selected category -> ", selected_category)
#         print("Here are all the recipes. Pick one to delete: ")
#         selected_recipe = recipe.get_recipe(selected_category[1])
#         print("selected_recipe -> ", selected_recipe)
#         recipe.delete_recipe(selected_category, selected_recipe)

#     # Create recipe category
#     elif selected_action_number == 4:
#         recipe_category.create_category()

#     # Delete recipe category
#     elif selected_action_number == 5:
#         recipe_category.delete_category()
#     # End program
#     elif selected_action_number == 6:
#         exit()
#     else:
#         print("Invalid selection. Please select a valid number. ")
