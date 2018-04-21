import string
import itertools
from .rotor import Rotor
from .reflector import Reflector


class Enigma:
    alphabet = list(string.ascii_uppercase)
    rotors = []
    reflector = None
    key = ''

    def __init__(self, key):
        self.set_key(key)

    def __test(self):
        print(self.key)

    def add_rotor(self, element):
        self.rotors.append(element)

    def add_reflector(self, reflector):
        self.reflector = reflector

    def set_key(self, key):
        self.key = key

        for letter in reversed(self.key):
            rotor = Rotor(self)
            rotor.set_shift_by_letter(letter)
            self.add_rotor(rotor)

    def set_alphabet(self, alphabet):
        self.alphabet = list(alphabet)

    def encode(self, message):
        output = ''
        for letter in message:
            direction = 1
            prev = None
            should_rotate = True
            if self.reflector:
                sequence = [item for item in self.rotors + [self.reflector] + list(reversed(self.rotors))]
            else:
                sequence = self.rotors

            for item in sequence:
                print(letter)
                prev_shift = prev.shift if getattr(prev, 'shift', None) else 0
                if isinstance(item, Rotor):
                    if should_rotate:
                        should_rotate = item.rotate()
                    letter = item.encode(letter, direction, prev_shift)
                elif isinstance(item, Reflector):
                    letter = item.encode(letter, prev_shift)
                    direction = -1

                prev = item

            output += letter

        return output
