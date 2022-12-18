# generator can be used in while loop.
def custom_generators():
	yield 1
	yield 2
	yield 3


g = custom_generators()

value_1 = next(g)
print(value_1)


value_1 = next(g)
print(value_1)