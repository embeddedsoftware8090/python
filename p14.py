#Write a Python program to calculate number of days between two dates.
from datetime import date
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)#always greater than the first numbers
delta = last_date - first_date
print(delta.days)
