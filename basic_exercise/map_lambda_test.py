sq_lambda = lambda x: x ** 2

number_list: list[int] = [1, 2, 3, 4, 5]

squ_numb = map(sq_lambda, number_list)

print(list(squ_numb))
