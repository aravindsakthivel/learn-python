from functools import wraps


def start_end_decoration(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		print("start")
		result = func(*args, **kwargs)
		print("end")
		return result

	return wrapper


@start_end_decoration
def print_closure_decorator(info):
	return info


# print_closure_decorator("block")

# print(help(print_closure_decorator))
print(print_closure_decorator.__name__)
