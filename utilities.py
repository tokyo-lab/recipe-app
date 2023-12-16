import os


def clear_screen():
    # Clear the screen, platform independent
    os.system("cls" if os.name == "nt" else "clear")
