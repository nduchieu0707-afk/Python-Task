Name = input("What is your name: ")
Float = float(input("Enter a floating point number: "))
Float2 = float(input("Enter second floating point number: "))
Multiply = float(Float * Float2)

print(f"{Name} you gave numbers {Float} and {Float2}")
print(f"Multiplying first and second number will result in product {round(Multiply, 2)}")