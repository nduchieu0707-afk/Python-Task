print("Program starting.")
numbers = []
for x in input("Insert comma separated integers: ").split(','):
    try:
        numbers.append(int(x))
    except:
        print(f"Invalid value '{x}' detected.")
print(f"There are {len(numbers)} integers in the list.")
total = sum(numbers)
print(f"Sum of the integers is {total} and it's {'even' if total % 2 == 0 else 'odd'}")
print("Program ending.")