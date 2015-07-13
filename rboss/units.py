"""
This file contains the data and functions required for converting between common cooking units.

Cooking measurement units can be in two main catagories: mass and volumetric. 
Each mass units maps to the the number base units which is grams. 
Each volumetric unit maps to the number of base units which is litres.
"""

mass_units = {
	'g' : 1,
	'kg' : 1000,
	'lb' : 453.592
	}

volume_units = {
	'l' : 1,
	'ml' : 1e-3,
	'cup' : 250
	}

def convert_mass_units(from_unit, from_quantity, to_unit):
	try:
		return from_quantity * mass_units[from_unit] / mass_units[to_unit]
	except KeyError:
		raise ValueError("Invalid unit string")

def convert_volume_units(from_unit, from_quantity, to_unit):
	try:
		return from_quantity * volume_units[from_unit] / volume_units[to_unit]
	except KeyError:
		raise ValueError("Invalid unit string")

def get_mass_units():
	return mass_units.keys()

def get_volume_units():
	return volume_units.keys()

def get_all_units_string():
	unit_string = ""
	for mass_unit in get_mass_units():
		unit_string += (mass_unit + " ")
	for volume_unit in get_volume_units():
		unit_string += (volume_unit + " ")
	return unit_string
