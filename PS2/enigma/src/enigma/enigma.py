import string
import itertools
from .rotor import Rotor
from .reflector import Reflector


class Enigma:
    alphabet = list(string.ascii_uppercase)
    elements = []
    key = ''

    def __init__(self, key):
        self.set_key(key)

    def __test(self):
        print(self.key)

    def add_element(self, element):
        self.elements.append(element)

    def set_key(self, key):
        self.key = key

        for letter in self.key:
            rotor = Rotor(self)
            rotor.set_shift_by_letter(letter)
            self.add_element(rotor)

    def set_alphabet(self, alphabet):
        self.alphabet = list(alphabet)

    def encode(self, message):
        output = ''
        for letter in message:
            direction = 1

            for item in itertools.chain(reversed(self.elements), self.elements):
                print(letter)
                if isinstance(item, Rotor):
                    letter = item.encode(letter, direction)

                if isinstance(item, Reflector):
                    letter = item.encode(letter)
                    direction = -1

            output += letter

        return output
