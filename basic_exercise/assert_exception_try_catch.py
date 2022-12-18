x: int = 5

assert(x <= 0), "x is negative"

if x > 0:
	raise Exception("x is positive")

try:
	a = 5 / 0
	b = a + 4
except ZeroDivisionError as e:
	print(e)
except TypeError as e:
	print(e)
except Exception as e:
	print("exce", e)
else:
	print("Everything is fine")
finally:
	print("cleaning up")