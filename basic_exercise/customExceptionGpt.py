class CustomException(Exception):
	def __init__(self, x):
		self.x = x


def foo(x):
	if x != 0:
		raise CustomException(x)


try:
	foo(1)
except CustomException as e:
	print(f'x was {e.x}')
