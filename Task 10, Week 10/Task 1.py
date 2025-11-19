print("Program starting.")

filename = input("Insert filename: ")

numbers = []
with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            numbers.append(line)

print("# --- Vertically --- #")
for number in numbers:
    print(number)
print("# --- Vertically --- #")

print("# --- Horizontally --- #")
print(", ".join(numbers))
print("# --- Horizontally --- #")

print("Program ending.")