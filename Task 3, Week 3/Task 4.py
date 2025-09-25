Name = input("This is a program with simple menu, where you can choose which operation the program performs. Before the menu, please insert your name: ")
print("Options:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

choice = input("Your choice: ")
if choice == '1':
    print(f"Welcome {Name}")
elif choice == '2':
    print(f"Your name backwards is {Name[::-1]}")
elif choice == '3':
    print(f"The first character in name {Name} is {Name[0]}")
elif choice == '4':
    print(f"There are {len(Name)} characters in the name {Name}")
elif choice == '0':
    print("Exiting...")
else:
    print("Unknown option.")