def main():
    numbers = []
    while True:
        user_input = input("Insert a floating-point value (0 to stop): ")
        try:
            value = float(user_input)
            if value == 0:
                break
            numbers.append(value)
        except ValueError:
            print(f"Error! '{user_input}' couldn't be converted to float.")
    
    print(f"Total: {sum(numbers)}")
if __name__ == "__main__":
    main()