import time

def main():
    print("Program starting.")
    pause_duration = 0.0
    
    while True:
        print("Options:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")
        
        choice = input("Your choice: ")
        
        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            try:
                pause_duration = float(input("Insert pause duration (s): "))
            except:
                print("Invalid input")
        elif choice == "2":
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            print("Unpaused.")
        else:
            print("Invalid choice")
        print()
    
    print("Program ending.")

if __name__ == "__main__":
    main()