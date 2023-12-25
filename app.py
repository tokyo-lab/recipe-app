from utilities import get_actions

# import category
# import recipe


def get_action_name(action_number):
    actions_dict = get_actions()
    action_name = actions_dict.get(action_number, "Key not found")
    return action_name


user_action = input("Select an action: ")
print(type(user_action))
action_name = get_action_name(user_action)
print("user_action", user_action)
print("action_number", action_name)

# if action_number is not None:
#     print(f"The action number for '{user_action}' is {action_number}.")
# else:
#     print(f"Action '{user_action}' not found.")


# while True:
#     try:
#         user_choice = int(input("Select an action: "))
#         print("user choice: ", user_choice)
#         if user_choice == 1:
#             category = category.get_category()
#             recipe.get_recipe(category)
#         elif user_choice == 2:
#             recipe.create_recipe()
#         else:
#             print("Invalid selection. Please select a valid number.")
#     except ValueError:
#         print("Invalid input. Please enter a number.")
