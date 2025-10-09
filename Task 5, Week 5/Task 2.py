def main():
    print("Program starting.")
    print()
    word = input("Insert word: ")
    frameWord(word)
    print("Program ending.")
    return None

def frameWord(PWord):
    print('*' * (len(PWord) + 4))
    print(f"* {PWord} *")
    print('*' * (len(PWord) + 4))
    return None

main()