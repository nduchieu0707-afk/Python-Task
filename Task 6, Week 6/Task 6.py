LOWER_ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shiftCharacter(characters, alphabet):
    if characters in alphabet:
        index = alphabet.index(characters)
        shifted_index = (index + 13) % len(alphabet)
        return alphabet[shifted_index]
    return characters

def rot13(text):
    result = ""
    for characters in text:
        if characters in LOWER_ALPHABETS:
            result += shiftCharacter(characters, LOWER_ALPHABETS)
        elif characters in UPPER_ALPHABETS:
            result += shiftCharacter(characters, UPPER_ALPHABETS)
        else:
            result += characters
    return result

def writeFile(filename, content):
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(content)

def main_program():
    print("Program starting.")

    rows = []
    print("Collecting plain text rows for ciphering.")
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)

    Ciphered = [rot13(row) for row in rows]

    print("\n#### Ciphered text ####")
    for text in Ciphered:
        print(text)

    filename = input("\nInsert filename to save: ")
    content = "\n".join(Ciphered) + "\n"
    writeFile(filename, content)
    print("Ciphered text saved!")

    print("Program ending.")

if __name__ == "__main__":
    main_program()