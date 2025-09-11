Task 1:

print("Hello Python program!")

Task 2:
Name1 = "John "
print(Name1)
Name2 = "Harry"
print(Name2)
print(Name1 + Name2)
print(f"{Name1}is eating ice cream with {Name2}")
print(f"{Name1}and {Name2} are friends") 

Task 3:
Name = input("What is your name: ")
print(f"Hi there {Name}")

Task 4:
Num1 = 47
Num2 = 102

Sum = Num1 + Num2
Diff = Num2 - Num1
Product = Sum * Diff
Product2 = (Num1 + Num2) * (Num2 - Num1)

print(f"{Num1} + {Num2} = {Sum}")
print(f"{Num2} + {Num1} = {Diff}")

print(f"{Sum} * {Diff} = {Product}")
print(f"({Num1} + {Num2}) * ({Num2} - {Num1}) = {Product2}")

Task 5:
print("Calculate the area of a wall.")
Feed = input("Enter the width in meters: ")
Width = int(round(float(Feed)))

Feed = input("Enter the height in meters: ")
Height = int(round(float(Feed)))

print("Result:")
print(f"Width is {Width} m and height is {Height} m.")
Area = Width * Height
print(f"The wall will be {Area} square meters.")

Task 6:
Feed = input("Insert an integer: ")
Value = int(Feed)
Remainder = Value % 2

print(f"Value is {Value}")
print(f"The remainder is {Remainder} when {Value} is divided by 2.")

Task 7:
print("Calculate fuel consumtion.")
Kilo = input("Enter travel distance(kilometers): ")
Lite = input("Enter fuel usage(liters): ")
Consumption = (int(Kilo) / int(Lite))
print(f"Fuel consumption is {int(Consumption)} l per 100 km")
