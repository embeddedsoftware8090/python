#Strings
#How would you confirm that 2 strings have the same identity?

# animals = ['python','gopher']
# more_animals = animals
# print(animals == more_animals)#=> True
# print(animals is more_animals)
# #=> Trueeven_more_animals = ['python','gopher']
# print(animals == even_more_animals)  #=> True
# print(animals is even_more_animals) #=> False
#--------------------------------------------------------------------------------
#How would you check if each word in a string begins with a capital letter?
#The istitle() function checks if each word is capitalized.

print( 'The Hilton'.istitle() ) #=> True
print( 'The dog'.istitle() ) #=> False
print( 'sticky rice'.istitle() ) #=> False

#------------------------------------------------------------------------------------------
# Check if a string contains a specific substring
#The in operator will return True if a string contains a substring.

print( 'plane' in 'The worlds fastest plane' ) #=> True
print( 'car' in 'The worlds fastest plane' ) #=> False

#------------------------------------------------------------------------------------------
# Count the total number of characters in a string
len('The first president of the organization..') #=> 19

#---------------------------------------------------------------------------------
#How to reverse a sentence in Python input by User

inputsentence = input("Please input a sentence :")
print(" ".join(reversed(inputsentence.split())))
#------------------------------------------------------------------------------------
#How to find the characters at an odd position in string input by User.
string = input("Enter the string : ")
outputString = ''
for i in range(len(string)):
    if(i % 2 == 0):
        outputString = outputString + string[i]
print("input string : ", string)
print("String after odd charcater :", outputString)


#--------------------------------------------------------------------------------------

#How to check string start with specific character enter by the user.

#we are using the startwith() method. It returns true if the string starts with a specified prefix or else returns false.

string = input("Enter the string : ")
result = string.startswith('Python')
print(result)

#----------------------------------------------------------
#How to remove all newline from the String.

inputString = '\nPython String\n with\n newline\n'
resultStr = inputString.replace("\n", "")
print(resultStr)

#-------------------------------------------------------------------
#Different ways to get the filename without extension

import os
FilePath = os.path.basename('/document/imp/salary.txt')
#file name with extension
print(FilePath)
#get file name and extension
print(os.path.splitext(FilePath))
#file name without extension
print(os.path.splitext(FilePath)[0])


#------------------------------------------------------------------------------
#How to replace all occurrence of sub-string in string

inputStr = "is the is Python is Program is"
modifiedStr = inputStr.replace('is', '')
print(modifiedStr)

#----------------------------------------------------------------------------------
#How to remove punctuation mark from list of string

listStr = ['', " 'Python'", " 'string'", " 'list of string'"]
modified_list = [item.replace("'", '')for item in listStr]
print(modified_list)

#----------------------------------------------------------------------------------

#How to find the number of matching characters in two string

import re
string1 = "Python"
string2 = "PythonProgram"
match_char_count = 0
for char in string1:

    if re.search(char,string2):
        match_char_count = match_char_count+1
print("matching charcter counts = ", match_char_count)

#---------------------------------------
#How to convert a string in list.

Countries = 'India, USA, Japan, Russia, UK'
print(list(Countries.split(', ')))


#-----------------------------
#How to find the Domain name from a string

import tldextract
Fullurl = 'https://www.devenum.com/cyber-security-tutorial/'
Domain_Information = tldextract.extract(Fullurl)
print("Domain Name: ", Domain_Information.domain)
print("Full Domain name: ", '.'.join(Domain_Information))

#---------------------------------------------------------
#How to convert all string elements of list to int.

numlst = ['20', '50', '100', '345', '609']
numlst = [int(num) for num in numlst ]
print ("all string elements to int in list : " ,numlst)


#-------------------
#Count Total numbers of upper case and lower case characters in input string

#here we are using isupper() to find upper case characters and islower() to find the lower case characters

string = input('Please enter the string: ')
upper_case= 0
lower_case = 0
for char in string:
    if char.isupper():
        upper_case+=1
    elif char.islower():
        lower_case+=1
print ("string entered by user : ", string)
print (" Total Upper case characters : ", upper_case)
print ("Total Lower case Characters : ", lower_case)


#------------------------------------------------
#Program to find vowels in a string

#Here we are checking upper case and lower case vowels characters.

input_string =input('Enter the string :')
vowels = "AaEeIiOoUu"
Vowel_found = [char
               for char in input_string if char in vowels]
print('no of vowels found =',len(Vowel_found))
print('Vowels found = ',Vowel_found)

#----------------------------------------------------
#How to reverse a user input string

input_string = input('Please Enter the string:')
reversed_str =''.join(reversed(input_string))
print('reversed string =',reversed_str)


#---------------------------------------------
#Program to sort a string in Python

input_string = input('Please Enter the string:')
sortedStr = sorted(sorted(input_string), key= str.upper)
print('sorted String =',sortedStr)

#-----------------------------------------------------
#How to print input string in upper case and lower case

input_string = input('Please Enter the string:')
print('input string lower case =',input_string.lower())
print('input string to upper case =',input_string.upper())


#--------------------------------------------------------------
#How To Extract URL From A String In Python?
#How to Extract URL from a string in Python? import re

def URLsearch(stringinput): #regular expression
    regularex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))))+(?:(([^\s()<>]+|(([^\s()<>]+))))|[^\s`!()[]{};:'\".,<>?«»“”‘’]))" #finding the url in passed string
    urlsrc = re.findall(regularex,stringinput) #return the found website url return [url[0] for url in urlsrc]
textcontent = 'text :a software website find contents related to technology https://devenum.com https://google.com,http://devenum.com' #using the above define function
print("Urls found: ", URLsearch(textcontent))


#---------------------------------------------------------------
#Convert Int To String In Python

#str() function is in built function in python that you can use to convert a number to string using these below steps.

variable = 55
print(type(variable))
string_num = str(variable)
print(type(string_num))

#---------------------------------------------------------------------
#Check if a string contains only numbers

print('80000'.isnumeric()) #=> True

#---------------------------------------------------------------------
#Split a string on a specific character
#The split() function will split a string on a given character or characters.
print('This is great'.split(' ')) #=> ['This', 'is', 'great']'not--so--great'.split('--') #=> ['not', 'so', 'great']

#-------------------------------------------------------------------------
#Check if the first character in a string is lowercase
print('aPPLE'[0].islower()) #=> True


#----------------------------------
#Reverse the string “hello world”
#We can split the string into a list of characters, reverse the list, then rejoin into a single string.

print(''.join(reversed("hello world"))) #=> 'dlrow olleh'

#--------------------------------------------------------
#Join a list of strings into a single string, delimited by hyphens
#Python’s join() function can join characters in a list with a given character inserted between every element.

print('-'.join(['a','b','c'])) #=> 'a-b-c'

#-----------------------------------------------------
#Check if all characters in a string conform to ASCII
#he isascii() function returns True if all characters in a string are included in ASCII.
print( 'Â'.isascii() ) #=> False print( 'A'.isascii() ) #=> True

#---------------------------------------------------
# Uppercase or lowercase an entire string
# upper() and lower() return strings in all upper and lower cases.

sentence = 'The Cat in the Hat'
print(sentence.upper()) #=> 'THE CAT IN THE HAT' sentence.lower() #=> 'the cat in the hat'

#----------------------------------------------------------------
#Uppercase first and last character of a string

animal = 'fish'
print(animal[0].upper() + animal[1:-1] + animal[-1].upper()) #=> 'FisH'

#Check if a string is all uppercase
#Similar to islower(), isupper() returns True only if the whole string is capitalized.

'Toronto'.isupper() #=> False 'TORONTO'.isupper() #= True

#-----------------------------------------------
#When would you use splitlines()?
#splitlines() splits a string on line breaks.

sentence = "It was a stormy night\nThe house creeked\nThe wind blew."
print(sentence.splitlines()) #=> ['It was a stormy night', 'The house creeked', 'The wind blew.']

#--------------------------------------------
#Give an example of string slicing
string = 'I like to eat apples'
print(string[:6]) #=> 'I like' string[7:13] #=> 'to eat' string[0:-1:2] #=> 'Ilk oetape' (every 2nd character)

#---------------------------------------------------------------------
#Convert an integer to a string
#Use the string constructor, str() for this.

print(str(5)) #=> '5'

#----------------------------------------------------------
#Check if a string contains only characters of the alphabet
#isalpha() returns True if all characters are letters.

print('One1'.isalpha() )
print('One'.isalpha())

#-----------------------------------------------------------
#Replace all instances of a substring in a string
#Without importing the regular expressions module, you can use replace().

sentence = 'Sally sells sea shells by the sea shore'
print(sentence.replace('sea', 'mountain')) #=> 'Sally sells mountain shells by the mountain shore'

#--------------------------------------------------------------------
#Check if all c
#Alphanumeric values include letters and integers.

print('Ten10'.isalnum()) #=> True
print('Ten10.'.isalnum()) #=> False

#-------------------------------------------------------------------------
#Remove whitespace from the left, right or both sides of a string
#lstrip(), rstrip() and strip() remove whitespace from the ends of a string.

string = ' string of whitespace '
print(string.lstrip()) #=> 'string of whitespace '
print(string.rstrip()) #=> ' string of whitespace'
print(string.strip()) #=> 'string of whitespace'


#-------------------------------------------------------------
#Check if a string begins with or ends with a specific character?
#startswith() and endswith() check if a string begins and ends with a specific substring.

city = 'New York'
print(city.startswith('New')) #=> True city.endswith('N') #=> False

#-------------------------------------
#Encode a given string as ASCII
#encode() encodes a string with a given encoding. The default is utf-8. If a character cannot be encoded then a UnicodeEncodeError is thrown.

print('Fresh Tuna'.encode('ascii')) #=> b'Fresh Tuna''Fresh Tuna Â'.encode('ascii') #=> UnicodeEncodeError: 'ascii' codec can't encode character '\xc2' in position 11: ordinal not in range(128)

#Check if all characters are whitespace characters
#isspace() only returns True if a string is completely made of whitespace.

print(''.isspace()) #=> False
print(' '.isspace())#=> True
print(' '.isspace()) #=> True
print(' the '.isspace())#=> False
#--------------------------------------------
#What does it mean for strings to be immutable in Python?

proverb = 'Rise each day before the sun'
print( id(proverb) ) #=> 4441962336proverb_two = 'Rise each day before the sun' + ' if its a weekday' print( id(proverb_two) ) #=> 4442287440