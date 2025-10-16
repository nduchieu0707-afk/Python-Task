import os

def rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

def main():
    locations = ["home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]
    
    print("Travel starting.")

    if os.path.exists("player_progress.txt"):
        with open("player_progress.txt", "r") as f:
            lines = f.readlines()
        current_line = lines[-1].strip().split(";")
        current_id = int(current_line[0])
        next_id = int(current_line[1])
        passphrase_cipher = current_line[2]
    else:
        with open("player_progress.txt", "w") as f:
            f.write("current_location;next_location;passphrase\n")
            f.write("0;1;qvfpvcyvar\n")
        current_id, next_id, passphrase_cipher = 0, 1, "qvfpvcyvar"
    
    print(f"Currently at {locations[current_id]}.")
    
    if next_id >= len(locations):
        print("All locations visited!")
        return
    
    print(f"Travelling to {locations[next_id]}...")
    print(f"...Arriving to the {locations[next_id]}.")
    print("Passing the guard at the entrance.")
    
    passphrase_plain = rot13(passphrase_cipher)
    print(f'"{passphrase_plain}!"')
    
    print("Looking for the message in the palace...")
    
    message_file = f"{next_id}_{passphrase_cipher}.gkg"
    if os.path.exists(message_file):
        with open(message_file, "r") as f:
            message_cipher = f.read().strip()
        
        message_plain = rot13(message_cipher)
        
        with open("player_progress.txt", "a") as f:
            f.write(f"{next_id};{next_id+1};{rot13(passphrase_cipher)}\n")
        
        output_file = f"{next_id}-{passphrase_plain}.txt"
        with open(output_file, "w") as f:
            f.write(message_plain)
        
        print("Ah, there it is! Seems cryptic.")
        print("[Game] Progress autosaved!")
        print("Deciphering Emperor's message...")
        print("Looks like I've got now the plain version copy of the Emperor's message.")
    else:
        print("Message file not found!")
    
    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()