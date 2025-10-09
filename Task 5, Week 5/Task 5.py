print("Program starting.")
print("Options:")
print("1 - Insert word")
print("2 - Show current word")
print("3 - Show current word in reverse")
print("0 - Exit")

def choice():
    Yourchoice = int(input("Your choice: "))
    Word = input("Insert word: ")
    if Yourchoice == 1:
        print(f"{Word}")
    return None
choice()