def main():
    print("Program starting.")
    
    try:
        red = int(input("Insert red: "))
        green = int(input("Insert green: "))
        blue = int(input("Insert blue: "))
        
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise ValueError("Value out of range")
        
        print("RGB Details:")
        print(f"- Red {red}")
        print(f"- Green {green}")
        print(f"- Blue {blue}")
        print(f"- Hex #{red:02x}{green:02x}{blue:02x}")
        
    except (ValueError, TypeError):
        print("Couldn't perform the designed task due to the invalid input values.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()