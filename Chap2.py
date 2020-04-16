# Variable and Simple Datatype
print("Hello world")
# 2-1. Simple Message: Store a message in a variable, and then print that
# message.
message = "How are You friend"
print(message)
# 2-2. Simple Messages: Store a message in a variable, and print that message.
# Then change the value of your variable to a new message, and print the new
# message.
message = "How are You friend"
print(message)
message = "Hello friend this is new message"
print(message)
# 2-3. Personal Message: Store a person’s name in a variable, and print a mes- 
# sage to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
name = "Muhammad Siraj"
print("Hello, "+name+" Would you like to learn python today")
# 2-4. Name Cases: Store a person’s name in a variable, and then print that per-
# son’s name in lowercase, uppercase, and titlecase.
name = "Siraj"
print(name.lower())
print(name.upper())
print(name.title())
# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n" , at least once.
name = "\t Muhammad \n \tSiraj"
print(name)
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip() ,
# rstrip() , and strip()
language = " Python     "
print(language)
print(language.strip())
print(language.lstrip())
print(language.rstrip())
# 2-8. Number Eight:\
print(5+3)
# 2-9. Favorite Number:
num = 7
print("my favorate number is {0}".format(num))