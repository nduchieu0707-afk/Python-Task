from math import prod

print("Program starting.\n\nCheck multiplicative persistence.")
num = input("Insert an integer: ")
steps = 0

while len(num) > 1:
    digits = list(num)
    product = prod(map(int, digits))
    print(f"{' * '.join(digits)} = {product}")
    num = str(product)
    steps += 1

print("No more steps.\n\nThis program took", steps, "step(s)\n\nProgram ending.")