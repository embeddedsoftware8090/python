#Write a Python program to display the current date and time
"""
from datetime import datetime #this is date and time library 
#from time import time
today = datetime.today()
print(today)

"""
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))