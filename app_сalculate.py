# -*- coding: utf-8 -*-

class Calculate(object):
	def add(self, x, y):
		return x + y
	def add_s(self, x, y): 
		"""Takes two integers and adds them together to produce
		the result.
		>>> c = Calculate()
		>>> c.add(1, 1)
		2
		>>> c.add(25, 125)
		150
		"""
		print(x, y)
		print(x+y)
		if type(x) == int and type(y) == int:
			return x + y
		else:
			raise TypeError("Invalid type: {} and {}".format(type(x),type(y)))

	def find_s(self, x, y):
		z = []
		for item_y in y:
			for item_x in x:

				if type(item_x) == int and type(item_y) == int:
					if item_x == item_y:
						item_y = item_y*2
				else:
					raise TypeError("Invalid type: {} and {}".format(type(item_x), type(item_y)))
			z.append(item_y)
		return z



if __name__ == '__main__':
	c = Calculate()
	#result = c.add_s(2, 2)
	#result = c.add(2, 2)
	#result = c.add_s("Hello", "World")
	result = c.find_s([1, 2], [2, 3])
	print(result)