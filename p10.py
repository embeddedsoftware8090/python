#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""n = 5
z = n + n * n + n * n * n
print(n,z)
"""
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
