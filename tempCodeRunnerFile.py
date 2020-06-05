active = True
while active:
    message = input("Enter Something \n")
    if message == 'quit':
        active = False
    else:
        print(message)