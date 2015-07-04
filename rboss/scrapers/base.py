"""
Abstract base class for Recipe Scrapers
"""
from bs4 import BeautifulSoup
import requests

class RecipeScraper:

	def __init__(self, url):
		response = requests.get(url)
		self.soup = BeautifulSoup(response.text)

	def get_ingredients(self):
		raise NotImplementedError("Please Implement this method")

	def get_steps(self):
		raise NotImplementedError("Please Implement this method")

	def get_steps_string(self):
		raise NotImplementedError("Please Implement this method")

