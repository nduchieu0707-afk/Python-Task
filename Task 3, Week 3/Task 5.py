print("Program starting")

print("Options: ")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exiting")

First = 1 
Second = 2 
Zero = 0 

choice = float(input("Your choice: "))
if choice == First:
    celcius = float(input("Inser the amount of Celsius: "))
    Fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius} °C equals to {Fahrenheit} °F")
elif choice == Second:
    fahrenheit  = float(input("Inser the amount of Fahrenheit: "))
    Celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit} °F equals to {round(Celsius, 1)} °C")
elif choice == Zero:
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending")