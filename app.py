from utilities import get_actions

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


while True:
    selected_action_number, selected_action_name = get_action_name()
    print("selected_action_number -> ", selected_action_number)
    print("selected_action_name -> ", selected_action_name)

    if selected_action_number == 1:
        selected_category = recipe_category.get_category()
        print("selected category -> ", selected_category)
        recipe.get_recipe(selected_category[1])
    elif selected_action_number == 2:
        selected_category = recipe_category.get_category()
        print("selected category -> ", selected_category)
        recipe.create_recipe(selected_category)
    else:
        print("Invalid selection. Please select a valid number. ")
