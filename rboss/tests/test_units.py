from ..units import *

def test_convert_g_kg():
	assert convert_mass_units('g', 1000, 'kg') == 1

def test_convert_l_ml():
	assert convert_volume_units('l', 1, 'ml') == 1000