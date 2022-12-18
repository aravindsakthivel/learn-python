class CustomCountCalls:
	def __init__(self, func):
		self.func = func
		self.num_calls = 0

	def __call__(self, *args, **kwargs):
		self.num_calls += 1
		print(f"The function has been called {self.num_calls} times")
		return self.func(*args, **kwargs)


@CustomCountCalls
def hello_cls():
	print("Hello")


hello_cls()
hello_cls()
