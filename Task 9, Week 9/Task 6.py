def save_lines(lines):
    filename = input("Insert filename: ")
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print(f"Lines saved to {filename}")

def main():
    lines = []
    print("Program starting.")
    
    try:
        while True:
            print("Options:")
            print("1 - Insert line")
            print("2 - Save lines")
            print("0 - Exit")
            choice = input("Your choice: ")
            
            if choice == "1":
                text = input("Insert text: ")
                lines.append(text)
                print()
            elif choice == "2":
                if len(lines) > 0:
                    save_lines(lines)
                    print()
                else:
                    print("No lines.\n")
            elif choice == "0":
                print("Program ending.")
                break
            else:
                print("Invalid choice. Please try again.\n")
                
    except KeyboardInterrupt:
        print("Keyboard interrupt and unsaved progress!")
        
        if len(lines) > 0:
            save_choice = input("Save before quit(y/n)?: ")
            if save_choice.lower() == "y":
                save_lines(lines)
        
        print("Program ending.")

if __name__ == "__main__":
    main()