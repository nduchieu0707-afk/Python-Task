print("Program starting. \nInsert two integers.")
Feed1 = int(input("Insert first integer: "))
Feed2 = int(input("Insert second integer: "))

print("Compare iserted integers.")
if (Feed1 > Feed2):
    print("First integer is greater.")
elif(Feed2 > Feed1):
    print("Second integer is greater.")
else:
    print("Both integers are the same")
print("")
print("Ađing integers together")
Sum = Feed1 + Feed2
print(f"{Feed1} + {Feed2} = {Sum}")

print("Checking the parity of the sum...")
Remainder = Sum % 2
if (Remainder == 0):
    print("Sum is even")
else:
    print("Sum is odd")
print("Program ending")