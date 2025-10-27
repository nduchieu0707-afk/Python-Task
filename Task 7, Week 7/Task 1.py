numbers = []

running = True
while running:
    Positive = int(input("Insert positive integer(negative stops): "))
    if Positive < 0:
        print("Stopped collecting positive integers.")
        running = False
    numbers.append(Positive)
print(f"Displaying {len(numbers)} integers:")
for i, num in enumerate(numbers):
    print(f"- Index {i} => Ordinal {i+1} => Integer {num}")