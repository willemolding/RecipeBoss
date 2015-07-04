"""
Parses recipes from taste.com to produce lists of ingredients and steps
"""
from base import RecipeScraper
from bs4 import BeautifulSoup
import requests

class TasteRecipeScraper(RecipeScraper):

	def get_ingredients(self):
		# first locate all the ingredients.
		ingredients = []
		for table in self.soup.find_all("ul", class_="ingredient-table"):
			for ingredient in table.find_all("li"):
				ingredients.append(ingredient.get_text(strip=True))
		return ingredients

	def get_steps(self):
		# locate each of the steps of the recipe
		steps = []
		for step in self.soup.find_all("p", itemprop="recipeInstructions"):
			steps.append(step.get_text(strip=True))
		return steps

	def get_steps_string(self):
		steps = self.get_steps()
		string = ''
		for step in steps:
			string += step
		return string

