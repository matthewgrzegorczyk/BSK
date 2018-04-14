from .rotor import Rotor
from .reflector import Reflector
from .alphabet import Alphabet


class Enigma:
    rotors = []
    alphabet_class = Alphabet()

    def __init__(self, key, rotor_count):
        self.key = key
        self.rotor_count = rotor_count
        self.add_rotors()
        self.reflector = Reflector()

    def add_rotors(self):
        for i in range(self.rotor_count):
            self.rotors.append(Rotor(
                self.alphabet_class.alphabet.index(self.key[i])
                )
            )
        
    def crypt(self, text):
        crypted_text = ''

        for char in text:
            crypted_char = char.upper()

            self.rotate_rotors()
            # Rotors in order (to reflector)
            for index in range(self.rotor_count):
                crypted_char = self.rotors[index].get_letter_by_input_letter_index(crypted_char)

            # Reflector
            crypted_char = self.reflector.resolve_letter(crypted_char)

            # Rotors in reversed order (from reflector)
            for rev_index in reversed(range(self.rotor_count)):
                self.rotors[rev_index].swap_alphabets()
                crypted_char = self.rotors[rev_index].get_letter_by_input_letter_index(crypted_char)

            crypted_text += crypted_char

        return crypted_text

    def rotate_rotors(self):
        most_right_rotor = 0

        self.rotors[most_right_rotor].rotate()
        for index in range(self.rotor_count):
            if self.rotors[index].is_full_cycle():
                if index == self.rotor_count:
                    break

                self.rotors[index + 1].rotate()