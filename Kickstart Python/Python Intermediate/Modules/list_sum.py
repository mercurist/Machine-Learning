from my_module import *
import my_module
numbers = [int(no) for no in input().split()]


print(my_module.printSum(numbers))


print(printSum(numbers))

print("imported module name =", my_module.__name__)
print("current module name  =", __name__)
