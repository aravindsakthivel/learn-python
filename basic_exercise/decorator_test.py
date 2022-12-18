def start_end_decoration(func):
	def wrapper():
		print("start")
		func()
		print("end")

	return wrapper


def print_closure():
	print("closure printed")


printed = start_end_decoration(print_closure)
printed()

print("------")


# using decorator printed can be done easily

@start_end_decoration
def print_closure_decorator():
	print("decorator closure printed")


print_closure_decorator()



