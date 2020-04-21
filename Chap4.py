# Working with lists
# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
Pizzas = ['Fazita','cheese','chickentikka']
for Pizza in Pizzas:
    print(Pizza)
# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
for pizza in Pizzas:
    print("I like "+pizza)
# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
for pizza in Pizzas:
    print("I like "+pizza)
print("I really love pizza")
# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
animals = ['Leopords','panther','Tiger']
for animal in animals:
    print(animal)
# •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
for animal in animals:
    print(animal+" is a danger animal")
# •	 Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!
for animal in animals:
    print(animal+" is a danger animal")
    print("Not a pet")

# List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)
# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive
for i in range(1,20):
    print(i)
    
# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.
# numbers = list(range(1,1000000))
# for number in numbers:
#     print(number)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
li = list(range(1,1000000))
print(min(li))
print(max(li))
print(sum(li))
# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
for i in range(0,20,2):
    print(i)
# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
l = [i*3 for i in range(3,30)]
for i in l:
    print(i)
# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
l = [i**3 for i in range(3,30)]
for i in l:
    print(i)
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes
lm = [i**3 for i in range(1,10)]
print(lm)