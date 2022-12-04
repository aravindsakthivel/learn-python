def print_crn_prv(val: int):
	print(f"Current Number 0 Previous Number 0 Sum: 0")
	for num in range(1, val):
		print(f"Current Number {num} Previous Number {num - 1} Sum: {num + num - 1}")


print_crn_prv(10)
