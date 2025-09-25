print("Program starting.")
print("Welcome to compare integer values.")

value = int(input("Insert value: "))

print("Options:")
print("1 - In one multi-branched decision")
print("2 - Independent if-statement decisions")
print("0 - Exit")

choice = int(input("Your choice: "))

original = value

if choice == 0:
    print("Exiting...")
elif choice == 1:
    if value >= 400:
        value += 44
    elif value >= 200:
        value += 22
    elif value >= 100:
        value += 11
    print(f"Result is: {value}")
elif choice == 2:
    if value >= 400:
        value += 44
    if value >= 200:
        value += 22
    if value >= 100:
        value += 11
    print(f"Result is: {value}")
else:
    print("Unknown option.")

print("Program ending.")