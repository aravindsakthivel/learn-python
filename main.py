# This is a sample Python script.
from itertools import combinations
import sys
# sys.path.append('test/test.py')

# testInside.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


async def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    info = 2 + 2
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# test.test_key()

list_nu: list = [1, 2, 3, 4]

comb = combinations(list_nu, 3)
print(list(comb))

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
