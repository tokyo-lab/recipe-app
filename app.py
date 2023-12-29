import utilities
from pathlib import Path

import recipe_category
import recipe


finish_program = False
category_path = Path("recipes")

while not finish_program:
    menu = utilities.start()
    if menu == 1:
        # show categories
        all_categories = recipe_category.show_categories(category_path)
        # select a category
        selected_category = recipe_category.select_category(all_categories)
        # show all recipes
        all_recipes = recipe.show_recipes(selected_category)
        # select a recipe
        selected_recipe = recipe.select_recipe(all_recipes)
        # read recipe
        recipe.read_recipe(selected_recipe)
        # go back to menu
        utilities.return_begining()
    elif menu == 2:
        # create recipe
        # show categories
        all_categories = recipe_category.show_categories(category_path)
        # select a category
        selected_category = recipe_category.select_category(all_categories)
        # create new recipe
        recipe.create_recipe(selected_category)
        # go back to menu
    elif menu == 3:
        # create a category
        recipe_category.create_category(category_path)
        # go back to menu
        utilities.return_begining()

    elif menu == 4:
        # delete recipe
        # show categories
        all_categories = recipe_category.show_categories(category_path)
        # select a category
        selected_category = recipe_category.select_category(all_categories)
        # show all recipes
        all_recipes = recipe.show_recipes(selected_category)
        # select a recipe
        selected_recipe = recipe.select_recipe(all_recipes)
        # delete recipe
        recipe.delete_recipe(selected_recipe)
        # go back to menu
        utilities.return_begining()

    elif menu == 5:
        # delete category
        # show categories
        all_categories = recipe_category.show_categories(category_path)
        # select a category
        selected_category = recipe_category.select_category(all_categories)
        # delete category
        recipe_category.delete_category(selected_category)
        # go back to menu
        utilities.return_begining()

    elif menu == 6:
        finish_program = True
