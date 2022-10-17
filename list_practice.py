#Program to find the max, min number from the list user input.

listlang = []
numbers = int(input('enter the number of items in list '))
for num in range(numbers):
    item = int(input('Entered number '))
    listlang.append(item)
print('entered list =',listlang)
print("Max number = :", max(listlang), "\nMin number :", min(listlang))




