# FUNCTIONS
# def greetings():
#     print("Hello")

# greetings()

# def greetUser(username):
#     print("Hello ",format(username))

# greetUser("Siraj")

# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
# def display_message():
#     print("In this chap i will learn about functions")

# display_message()
# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
# def favorite_book(title):
#     print("My Favorite book is "+ title)


# favorite_book("Python Crash Course")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

# def make_shirt(size,text):
#     print("The Size of your shirt is "+str(size)+" and text will printed is "+text)

# make_shirt(33,"Summers")
# make_shirt(size=38,text="Planets")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

# def make_shirt(size='large'):
#     print("The Size of your shirt is "+str(size))

# make_shirt()
# make_shirt(size='small')
# make_shirt(size='medium')

# def addit(a,b):
#     p = print(a+b)
#     return p

# addit(2,3)

# def buildPerson(fname,lname):
#     person = {'First':fname, 'Last':lname}
#     return person

# mucisian = buildPerson('Muhammad','Siraj')
# print(mucisian)

# def make_pizza(*toppings):
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#  """Build a dictionary containing everything we know about a user."""
#  profile = {}
#  profile['first_name'] = first
#  profile['last_name'] = last
#  for key, value in user_info.items():
#      profile[key] = value
#      return profile
# user_profile = build_profile('albert', 'einstein',
#  location='princeton',
#  field='physics')
# print(user_profile)

import pizza

pizza.make_pizza("Extra Cheese")
pizza.make_pizza(16,'pepproni')

from pizza import make_pizza

make_pizza(19,'garlic')

from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')