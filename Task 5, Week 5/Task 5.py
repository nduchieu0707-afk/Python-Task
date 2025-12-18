def main():
    print("Program starting.")
    current_word = "" 
    
    while True:
        print("\nOptions:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            current_word = input("Insert word: ")
        elif choice == "2":
            if current_word == "":
                print("Current word - \"\"")
            else:
                print(f"Current word - \"{current_word}\"")
        elif choice == "3":
            if current_word == "":
                print("Current word - \"\"")
            else:
                print(f"Word reversed - \"{current_word[::-1]}\"")
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Unknown option!")
    print("Program ending.")
main()

