#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
"""
a = 17
b =int(input("Enter the numbers of b: "))#input always take as strings input
if b > a :
    print(int(a))
else :
    print(int(b))
    """
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

        #print(difference(22))
print(difference(14))
print(difference(20))
print(difference(30))
print(difference(40))
print(difference(50))
