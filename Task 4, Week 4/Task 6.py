print("Program starting.")
number = int(input("Insert a positive integer: "))
sequence = [str(number)]
steps = 0

while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    sequence.append(str(number))
    steps += 1

print(" -> ".join(sequence))
print(f"Sequence had {steps} total steps.\n") 
print("Program ending.")