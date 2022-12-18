list_a: list = [10, 20, 25, 30, 35]
list_b: list = [40, 45, 60, 75, 90]

list_c: list = list_a + list_b

final_list: list = list(set(list_c))

print(final_list)
