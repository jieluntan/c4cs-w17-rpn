import unittest
import rpn
import colored
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_exponent(self):
		result = rpn.calculate('2 6 ^')
		self.assertEqual(64, result)
		print("%s Result: %s", result, (colored.fg('red'),colored.attr('reset')))
	def test_exponent(self):
		result = rpn.calculate('2 2 ^')
		self.assertEqual(4, result)
		print("%s Result: %s", result, (colored.fg('red'),colored.attr('reset')))
