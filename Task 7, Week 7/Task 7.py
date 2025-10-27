class EnigmaMachine:
    def __init__(self):
        self.rotors = []
        self.reflector = ""
        self.positions = [0, 0, 0]
        
    def load_config(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("Rotor1:"):
                    self.rotors.append(line.strip().split(":")[1])
                elif line.startswith("Rotor2:"):
                    self.rotors.append(line.strip().split(":")[1])
                elif line.startswith("Rotor3:"):
                    self.rotors.append(line.strip().split(":")[1])
                elif line.startswith("Reflector:"):
                    self.reflector = line.strip().split(":")[1]
    
    def rotate_rotors(self):
        self.positions[0] = (self.positions[0] + 1) % 26
        if self.positions[0] == 0:
            self.positions[1] = (self.positions[1] + 1) % 26
            if self.positions[1] == 0:
                self.positions[2] = (self.positions[2] + 1) % 26
    
    def forward_pass(self, char):
        for i in range(3):
            pos = self.positions[i]
            idx = (ord(char) - ord('A') + pos) % 26
            char = self.rotors[i][idx]
        return char
    
    def reflector_pass(self, char):
        idx = ord(char) - ord('A')
        return self.reflector[idx]
    
    def reverse_pass(self, char):
        for i in range(2, -1, -1):
            pos = self.positions[i]
            idx = self.rotors[i].index(char)
            char = chr((idx - pos) % 26 + ord('A'))
        return char
    
    def encrypt_char(self, char):
        if not char.isalpha():
            return char
        
        char = char.upper()
        self.rotate_rotors()
        
        char = self.forward_pass(char)
        
        char = self.reflector_pass(char)
        
        char = self.reverse_pass(char)
        
        return char
    
    def encrypt_text(self, text):
        self.positions = [0, 0, 0]
        result = []
        
        for char in text:
            if char.isalpha():
                encrypted_char = self.encrypt_char(char)
                result.append(encrypted_char)
                print(f'Character "{char}" illuminated as "{encrypted_char}"')
            else:
                result.append(char)
        
        return ''.join(result)

def main():
    enigma = EnigmaMachine()
    
    filename = input("Insert config(filename): ")
    enigma.load_config(filename)
    
    plugs = input("Insert plugs (y/n)?: ")
    if plugs.lower() == 'y':
        print("No extra plugs inserted.")
    else:
        print("No extra plugs inserted.")
    
    print("Enigma initialized.\n")
    
    while True:
        text = input("Insert row (empty stops): ")
        if not text:
            break
        
        encrypted = enigma.encrypt_text(text)
        print(f'Converted row - "{encrypted}".\n')
    
    print("Enigma closing.")

if __name__ == "__main__":
    main()