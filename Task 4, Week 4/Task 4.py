count = 0
character_count = 0
running = True
while running:
    Loop = input("Insert word (empty stops): ")
    if Loop == "":
        running = False
    else:
        count += 1
        character_count += len(Loop)
print("You inserted: ")
print(f"Words: {count}")
print(f"Characters: {character_count}")