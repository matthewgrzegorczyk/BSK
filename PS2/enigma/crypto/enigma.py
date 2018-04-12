from .rotor import Rotor


class Enigma:
    rotors = []

    def __init__(self, key, rotor_count):
        self.key = key
        self.rotor_count = rotor_count
        self.add_rotors()

    def add_rotors(self):
        for i in range(self.rotor_count):
            self.rotors.append(Rotor(self.key[i]))
        
    def crypt(self, text):
        modified_text = ''
        for char in text:
            for rotor in range(len(self.rotors)):
                modified_text += self.rotors[rotor].resolve_letter(char)

        return modified_text
