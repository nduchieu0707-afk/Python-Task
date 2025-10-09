print("Program starting.")

total_word = []
total_characters = 0

while True:
    word = input("Insert word(empty stops): ")
    
    if word == "":
        break
    
    total_word.append(word)
    total_characters += len(word)

word_count = len(total_word)
average_length = total_characters / word_count if word_count > 0 else 0

print(f"- {word_count} Words")
print(f"- {total_characters} Characters")
print(f"- {average_length:.2f} Average word length")
print("Program ending.")