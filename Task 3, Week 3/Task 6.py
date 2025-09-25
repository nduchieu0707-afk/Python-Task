print("Program starting.")
print("Welcome to the unit converter program!")

print("Options: ")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exiting")

choice1 = input("Your choice: ")

if choice1 == '0':
    print("Exiting...")
    print("Program ending.")
elif choice1 == '1':
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == '1':
        m = float(input("Insert meters: "))
        print(f"{m} m is {m/1000} km")
    elif choice2 == '2':
        km = float(input("Insert kilometers: "))
        print(f"{km} km is {km*1000} m")
    elif choice2 == '0':
        print("Exiting...")
    else:
        print("Unknown option.")
elif choice1 == '2':  
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choice2 = input("Your choice: ")
    if choice2 == '1':
        g = float(input("Insert grams: "))
        print(f"{g} g is {round(g/453.592, 1)} lb")
    elif choice2 == '2':
        lb = float(input("Insert pounds: "))
        print(f"{lb} lb is {round(lb*453.592, 1)} g")
    elif choice2 == '0':
        print("Exiting...")
    else:
        print("Unknown option.")
else:
    print("Unknown option.")