
from ..recipe import Recipe

def test_recipe():
	ingredient_strings = ['3 eggs', '1/2 cup sugar']
	steps_string = "Preheat the oven. Cream eggs and sugar until pale."
	recipe = Recipe(ingredient_strings, steps_string)
	print [(ing.get_quantity(), ing.get_unit(), ing.get_keywords()) for ing in recipe.get_ingredients()]
	print recipe.get_steps_sents()
	print recipe.get_nouns()