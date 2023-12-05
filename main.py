# This is a sample Python script.
from my_module_9 import calculation


def running_calculation(x, y):
    print("Plus:")
    print(calculation.plus(x, y))
    print("Minus:")
    print(calculation.minus(x, y))
    print("Divide:")
    print(calculation.divide(x, y))
    print("multiple:")
    print(calculation.multiple(x, y))


running_calculation(10, 5)
