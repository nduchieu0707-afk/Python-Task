#Length = input("Insert a closed compound word: ")
#print(f"the word you inserted is {Length} and in reverse it is {Length[::-1]}")
#print(f"The inserted word length is {len(Length)}")
#print(f"The last chapter is {Length[-1]}")

#print("Take substring from the inserted word by inserting...")
#start = int(input("1) Starting point: "))
#end = int(input("2) Ending point: "))
#step = int(input("3) Step size: "))

#Substring = Length[start:end:step]

#print(f"The word '{Length}' sliced to the defined substring is '{Substring}'.")

print("Program starting.")

Length = input("Insert a closed compound word: ")
print(f"The word you inserted is '{Length}' and in reverse it is '{Length[::-1]}'.")
print(f"The inserted word length is {len(Length)}")
print(f"Last character is '{Length[-1]}'")

print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))

Substring = Length[start:end:step]
print(f"The word '{Length}' sliced to the defined substring is '{Substring}'.")

print("Program ending.")