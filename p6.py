#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

from numpy import number
numbers = 3,5,7,23
result = list(numbers)
print("list :",result)
print("tuple:",str(numbers))
"""
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
"""