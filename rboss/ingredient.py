"""
Defines the ingredient class which is created with a string and deals with converting this into a quantity, unit and some keywords.
"""
from units import *
from pyparsing import *

class Ingredient:

	def __init__(self, string):
		"""
		Creates an aware ingredient object given a natural language string
		"""
		self.string = string
		self.parse = self._idenfify_quantities(self.string)


	def get_quantity(self):
		return self.parse.get('quantity', '').strip()

	def get_unit(self):
		return self.parse.get('unit', '').strip()

	def get_keywords(self):
		return [word.strip() for word in self.parse.get('word', None)]


	def _idenfify_quantities(self, string):
	    """
	    Identifies ingredient quantities, units and keywords from an ingredient list item
	    """
	    units = get_all_units_string()

	    quantity = Combine(Word( nums + '/.-') + Optional(White() + Word( nums + '/.-'))).setResultsName('quantity').setName('quantity') #the quantity of ingredient.
	    unit = Combine(oneOf(units) + Optional('s') + White()).setResultsName('unit').setName('unit') #the unit.
	    word = Word(alphas+"-.?#!_").setName('word').setResultsName('word',listAllMatches=True) #the words describing the ingredient.
	    clarifier = Suppress(Regex(r" ?\(.*\) ?")).setName('clarifier').leaveWhitespace() # a clarifier e.g "1 cup (250ml)". We want to suppress these.

	    ingredient = Optional(quantity) + Optional(unit) + Optional(clarifier) + OneOrMore( word + Optional(clarifier)) 

	    return ingredient.parseString(string)
