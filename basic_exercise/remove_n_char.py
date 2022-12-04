def remove_n_char(char: str, n: int):
	if n < len(char):
		print(char[n:])
	else:
		print("Out of range operation", n)


val_char: str = "pynative"
remove_n_char(val_char, 2)
