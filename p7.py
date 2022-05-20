#Write a Python program to accept a filename from the user and print the extension of that
"""sample_input =input("Enter the filename : ")
print("output :",sample_input)

"""
#from distutils import extension

filename = input("Input the Filename: ")
extension = filename.split(".")#The split() method splits a string into a list
print ("The extension of the file is : " + repr(extension[-1])) #repr() function returns the string representation of the value passed
