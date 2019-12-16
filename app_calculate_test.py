# -*- coding: utf-8 -*-

import unittest
from app_calculate import Calculate

class TestCalculate(unittest.TestCase):
	def setUp(self):
		self.c = Calculate()

	#def test_add_method_returns_correct_result(self):
	#	self.assertEqual(4, self.c.add(2,2))
		#self.assertEqual(4, self.c.add(2,3))

	#def test_add_method_returns_correct_result(self):
	#	self.assertEqual("HelloWorld", self.calc.add_s("Hello","World"))

	#def test_add_method_raises_typeerror_if_not_ints(self):
	#	self.assertRaises(TypeError, self.calc.add_s, "Hello","World")

	#def test_assert_raises(self):
	#	self.assertRaises(AttributeError, [].get)

	#def test_assert_raises(self):
	#	with self.assertRaises(AttributeError):
	#		[].get

	def test_add_method_returns_correct_result(self):
		self.assertEqual([4, 3], self.c.find_s([1, 2], [2, 3]))

	def test_add_method_returns_correct_result(self):
		self.assertEqual([4, 3], self.c.find_s([1, 2], [2, 3]))


if __name__ == '__main__':
	unittest.main()