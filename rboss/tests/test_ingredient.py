
from ..ingredient import Ingredient

def test_create_ingredient():
	ing = Ingredient("1 cup plain flour")
	assert(ing.get_quantity() == '1')
	assert(ing.get_unit() == 'cup')
	assert(ing.get_keywords() == ['plain', 'flour'])