from .rotor import Rotor
from .reflector import Reflector


class Enigma:
    rotors = []

    def __init__(self, key, rotor_count):
        self.key = key
        self.rotor_count = rotor_count
        self.add_rotors()
        self.reflector = Reflector()

    def add_rotors(self):
        for i in range(self.rotor_count):
            self.rotors.append(Rotor(self.key[i]))
        
    def crypt(self, text):
        crypted_text = ''

        for char in text:
            crypted_char = char

            # Rotors in order (to reflector)
            for index in range(self.rotor_count):
                crypted_char = self.rotors[index].resolve_letter(crypted_char)

            # Reflector
            crypted_char = self.reflector.resolve_letter(crypted_char)

            # Rotors in reversed order (from reflector)
            # for rev_index in reversed(range(self.rotor_count)):
                # crypted_char = self.rotors[rev_index].resolve_letter_backwards(crypted_char)

            crypted_text += crypted_char

        return crypted_text
