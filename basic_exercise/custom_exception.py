class CustomReg(Exception):
	pass


class CustomWithWords(Exception):
	"""This gets printed"""
	pass


class CustomException(Exception):
	def __init__(self, x, b):
		self.x = x
		self.b = b


def test_value(x):
	if x > 0:
		raise CustomException("X is large", x)
	else:
		raise CustomReg("Reg test")


try:
	test_value(5)
except CustomException as e:
	print(e.x)
except CustomReg as e:
	print(e)
