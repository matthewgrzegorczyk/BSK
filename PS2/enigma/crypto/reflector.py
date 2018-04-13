import string
from random import shuffle

class Reflector:

    def __init__(self):
        self.alphabet = self.init_alphabet()

    def init_alphabet(self):
        mixed_letters = list(string.ascii_uppercase)
        shuffle(mixed_letters)

        alphabet = {}
        for char, index in string.ascii_uppercase:
            alphabet[char] = mixed_letters[index]

        return alphabet

    def resolve_letter(self, letter):
        return self.alphabet[letter]

    def get_alphabet(self):
        return self.alphabet
