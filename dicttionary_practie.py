# dictionary interview questions

# Get keys[“name”, “age”] from dictionary and create new dictionary
animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"
}
outDict = {key: animaldict[key] for key in ["name", "age"]}
print(outDict)

#-------------------------------------------------
# Program to delete set of keys from Dictionary
# keys to delete : [“name”, “age”]

animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"

}
outDict = {key: animaldict[key] for key in animaldict.keys() - ["name", "age"]}
print(outDict)

#-----------------------------------------------------------------------
# What will the output of following Program
dictlang = {'c#': 6, 'GO': 89, 'Python': 4, 'Rust': 10}
for _ in sorted(dictlang):
    print(dictlang[_])

#------------------------------------------------------------
# How to change the name of key in dictionary.
# Here we have to change the key “name “ to “Animalname” in nested dictionary.
animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"
}
animaldict['Animalname'] = animaldict.pop('name')
print(animaldict)

#-----------------------------------------------------------
# How to change the value of any key in nested dictionary
# here,we are changing the age of animal “cat” in nested “Animal 1” dictionary.
animaldict = {
    "animal": {
        "name": "Dog",
        "age": 5,

    },
    "animal1": {
        "name": "Cat",
        "age": 2,

    },
    "animal2": {
        "name": "Rabbit",
        "age": 1,

    },

}
animaldict["animal1"]['age'] = 5
print(animaldict)

#------------------------------------------------------------------------------
# How to delete a key from Dictionary
fruitsDict = {
    'Apple': 100,
    'Orange': 200,
    'Banana': 400,
    'pomegranate': 600
}
if 'Apple' in fruitsDict:
    del fruitsDict['Apple']
print('Dict after deleting key =', fruitsDict)

#--------------------------------------------------------------------
# How to get min and max keys corresponding to min and max value in Dictionary
fruitsDict = {
    'Apple': 100,
    'Orange': 200,
    'Banana': 400,
    'pomegranate': 600
}
print('min value key = ', min(fruitsDict, key=fruitsDict.get))
print('max value key =', max(fruitsDict, key=fruitsDict.get))

#----------------------------------------------------------------
# how to concatenate multiple dictionary in one
# Using for-loop and update() we can concatenate multiple dictionary in one
Fruit = {'Apple': 100, 'banana': 5}
Subject = {'Math': 100, 'English': 98}
animal = {'name': 'Rabbit', 'age': 1}
conacte_Dict = {}
for dict in (Fruit, Subject, animal): conacte_Dict.update(dict)
print(conacte_Dict)

#-------------------------------------------------------------------------
# How to sum all elements of Dictionary
# Using the sum() method we can sum the Dictionaries elements.
Fruit = {'Apple': 100, 'banana': 5, 'orange': 45, 'Guava': 60}
print('sum of dict elements = ', sum(Fruit.values()))


#---------------------------------------------------------------------------
# How to multiply all elements of dictionary
FruitDict = {'Apple': 10, 'banana': 5, 'orange': 4, 'Guava': 6}
mutiply_res = 1
for key in FruitDict:
    mutiply_res = mutiply_res * FruitDict[key]

print('mutiplication of dict elements = ', mutiply_res)


#--------------------------------------------------------------------------
# How to sort a dictionary by key
FruitDict = {'Apple': 10, 'Banana': 5, 'Orange': 4, 'Guava': 6}
print('sorted dictionary = ')
for key in sorted(FruitDict):
    print("%s: %s" % (key, FruitDict[key]))

#_-------------------------------------------------------------------------
# How do we find highest 2 values in a dictionary
from heapq import nlargest

FruitDict = {'Apple': 600, 'Banana': 515, 'Orange': 214, 'Guava': 1116}
two_highest_values = nlargest(2, FruitDict, key=FruitDict.get)
print(two_highest_values)

#---------------------------------------------------------------------------
# How to convert a string in dictionary
from collections import defaultdict, Counter

mystring = 'DictExample'
string_dict = {}

for word in mystring:
    string_dict[word] = string_dict.get(word, 0) + 1
print(string_dict)

#----------------------------------------------------------------------------------------
# How to print Dictionary as table
Dict_tab = {'Students': ['Rack', 'Jack', 'John'], 'Fruit': ['Apple', 'Banana', 'Orange'],
            'Subject': ['Phy', 'Math', 'English']}

for row in zip(*([key] + (value) for key, value in sorted(Dict_tab.items()))):
    print(*row)
#----------------------------------------------------------------------------------
# How to remove space between dictionary keys.
myDict = {'Fr   uit': ['Apple', 'Banana', 'Orange'], 'Sub   ject': ['Phy', 'Math', 'English']}
myDict = {i.translate({32: None}): j for i, j in myDict.items()}
print("dict after remove space = ", myDict)

#----------------------------------------------------------------------------
# How to remove no value items from Dictionary.
mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
OutDict = {key: value for (key, value) in mutidict.items() if value is not None}
print(OutDict)

#-----------------------------------------------------------------------------------
# How to filter dictionary based on value.
empdict = {'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
filterEmpDict = {key: value for (key, value) in empdict.items() if value <= 80000}
print('Fillter dictionary = ', filterEmpDict)

#-----------------------------------------------------------------------------------
# How to convert nested tuples into custom key dictionary
empdict = [(('Salary', 'of', 'Racx'), 12000), (('Salary', 'of', 'Tax'), 80000)]
output = {' '.join(key): val for key, val in empdict}
print("Custom key dictionary : ", output)

#---------------------------------------------------------------------------------
# How to check number of keys have same value.
empdict = {'Racx': 12000, 'Max': 80000, 'Stack': 80000, 'John': 80000, }
valuetofind = 80000
count = sum(val == valuetofind for val in empdict.values())
print("number of keys have same value : ", count)

#--------------------------------------------------------------------------------
# How to convert dictionary object into string
personDict = {"Name": "Simulen",
              "City": "CA",
              "Country": "USA"}
print('Type before conversion = ', type(personDict))
dicttoString = str(personDict)
print("\ntype after conversion = ", type(dicttoString))
print("\ndict object to string = ", dicttoString)
#--------------------------------------------------------------------------------
# Program to add multiple keys into dictionary
personDict = {'person': {"Name": "Simulen",
                         "City": "CA",
                         "Country": "USA"}}
personDict['person']['Company'] = 'Morgan stanely'
print("Dictionary after adding key =\n", personDict)

#-------------------------------------------------------------------------------------
##Create Dictionary with integer keys
# create a dictionary with data integer keys
first_dict = {1: 'Dog', 2: 'cat', 3: 'rat'}
print("dictionary with integer key:\n ")
print(first_dict)
#-----------------------------------------------------------------------------------
# How to Create Dictionary using dict() from a list of tuples?
# dictionary with data

first_dict = {1: 'apple', 2: 'orange', 3: 'kiwi'}
print("dictionary with data: ")
print(first_dict)

#--------------------------------------------------------------------
# dictionary from a list of tuple
first_dict = [(1, 'apple'), (2, 'orange'), (3, 'kiwi')]
print("dictionary from a list of tuples: ")
print(first_dict)

#--------------------------------------------------------------------
# Add new key-value pair Using subscript notation
dict_sub = {}
dict_sub['math'] = 100
print('after adding value to dictionary =', dict_sub)

#-----------------------------------------------------------------
# How to loop over python dictionary?
# *For loop : To access value by key of Python dictionary
first_dict = {1: 'apple', 2: 'orange', 3: 'kiwi'}
print("Keys and Values: ")
for key in first_dict:
    print(key, first_dict[key])

#----------------------------------------------------------------
# Creating a new dictionary from iterable(list)
keys_lst = ['at', 'an', 'am', 'as']
values_lst = [11, 12, 13, 14, 15]
dict_sub = {key: val for (key, val) in zip(keys_lst, values_lst)}
print('dictionary from lsit iterable:\n', dict_sub)


#------------------------------------------------------------------------------
# How to use dictionary comprehension with condition?
my_dict = {'at': 1, 'as': 20, 'am': 30, '15': 4, 'e': 5}

dict_output = {key: val for (key, val) in my_dict.items() if val % 2 == 0}

print(dict_output)

# #output:

# {'as': 20, 'am': 30, '15': 4}

#----------------------------------------------------------------------------
# What is Python dictionary copy() method?
# The Python dictionary copy() method return a copy of existing dictionary.
original_dict = {'at': 12, 'as': 20, 'am': 30, 'rat': 16}
copy_dict = original_dict.copy()
print(copy_dict)
# output
# {'at': 12, 'as': 20, 'am': 30, 'rat': 16}

