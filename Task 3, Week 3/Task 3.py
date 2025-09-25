Name = input("This is a program with simple menu, where you can choose which operation the program performs. Before the menu, please insert your name: ")
print("Options:")
print("1 - Print welcome message")
print("0 - Exit")
choice = input("Your choice: ")
if choice == '1':
    print(f"Welcome {Name}")
elif choice == '0':
    print("Exiting...")
else:
    print("Unknown option.")