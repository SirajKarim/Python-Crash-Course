# Conditionals 
# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •	 Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
car = input()
if car == 'subaru':
    print('I predict true')
elif car == 'audi':
    print("I predict false")


num = input()
if num == 10:
     print("True")
else:
    print("false")
# •	 Tests using the lower() function
name = 'Siraj'
if(name == name.lower()):
    print(name)
# •	 Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
if num > 0:
    print("Psitive")
else:
    print("Negative")
# •	 Tests using the and keyword and the or keyword
if name == name.lower() and name.upper():
    print("Your name is "+ name)
# •	 Test whether an item is in a list
lst = ['Siraj','Ajmal','Hamza']
if 'Siraj' in lst:
    print("Yes True") 
# •	 Test whether an item is not in a list
if 'Akif' not in lst:
    print('No False')