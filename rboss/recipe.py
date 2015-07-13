"""
The class representing a single recipe. 

Recipes contain a list of ingredients and a list of steps. 

It contains methods for displaying in different formats and bulk converting units
"""
from ingredient import Ingredient
from textblob import TextBlob

class Recipe:

	def __init__(self, ingredient_strings, step_strings):
		self.ingredients = [Ingredient(string) for string in ingredient_strings]
		self.steps = TextBlob(step_strings)

	def get_ingredients(self):
		return self.ingredients

	def get_steps_sents(self):
		return self.steps.sentences


	def get_nouns(self):
		

