import os


def clear_screen():
    # Clear the screen, platform independent
    os.system("cls" if os.name == "nt" else "clear")


def get_actions():
    actions_dict = {
        1: "Read Recipe",
        2: "Create Recipe",
        3: "Delete Recipe",
        4: "Create Category",
        5: "Delete Category",
        6: "End Program",
    }
    # Print action options
    for index, action in actions_dict.items():
        print(f"[{index}] - {action}")
    return actions_dict
