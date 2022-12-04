numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def match_fn(list_val: list) -> bool:
	if list_val[0] == list_val[len(list_val) - 1]:
		return True
	else:
		return False


print(match_fn(numbers_x))
print(match_fn(numbers_y))
