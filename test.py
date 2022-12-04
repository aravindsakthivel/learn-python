def say_hi():
    print("Hello")


integer_val = 5
print(integer_val)

def new_val():
    integer_val = "abc"
    print(integer_val)

try:
   print(5)
except Exception as err:
    print(err)

test_key = "may"

list_input = {test_key: 5, "june": 6}
print(list_input["may"], list_input)
for info in list_input:
    print(info)
say_hi()
new_val()

