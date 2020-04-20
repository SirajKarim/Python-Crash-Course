# Lists
# 3-1. Names: Store the names of a few of your friends in a list called names . Print
# each person’s name by accessing each element in the list, one at a time.

names = ['Awais','Abdullah', 'Saqib']
print(names[0])
print(names[1])
print(names[2])
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the
# person’s name.
print("Good Evening {0}".format(names[0]))
print("Good night {0}".format(names[1]))
print("Good night {0}".format(names[2]))
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
fav = ["I would like to own toyota car","I would like to own honda bike"]
print(fav[0])
print(fav[1])

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
ges = ['Ajmal','Hamza','Abdal']
inv = ['You are invited for dinner','Come and enjoy dinner with me']
print(ges[0]+" "+inv[0])
print(ges[1]+" "+inv[0])
print(ges[2]+" "+inv[1])
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.
ges[2] = 'Ayaz'
print(ges[2]+" "+inv[1])
# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
ges.append('Ausaf')
ges.append('hamid')
ges.append('sohail')
# 46     Chapter 3
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
ges.insert(0,'Abdullah')
ges.insert(2,'Ajju')
ges.append("Akif")