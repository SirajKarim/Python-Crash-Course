# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
personalInfo = {
    "firstname": "Muhammad",
    "lastname" : "siraj",
    "age" : 22,
    "city" : "Karachi"
}
print(personalInfo["firstname"])
print(personalInfo["lastname"])
print(personalInfo["age"])
print(personalInfo["city"])
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
favoriteNum = {
    "Siraj": 7,
    "Shoaib": 5,
    "Ali" : 9
}
print(favoriteNum["Ali"])
print(favoriteNum["Siraj"])
print(favoriteNum["Shoaib"])

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. 
pro = {
    "variable":"A Container which hold values",
    "Conditionals":"Check the conditions "
}
print(pro["variable"])

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary
rivers = {
    "Nile":"Egypt",
    "Amazon":"South America",
    "yangtaz":"China"
}
for river in rivers:
    print(river)
for river in rivers:
    print(rivers[river])
# 6-6. Polling: Use the code in favorite_languages.py (page 104).

# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.