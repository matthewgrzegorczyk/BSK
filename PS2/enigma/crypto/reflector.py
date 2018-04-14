import string
from random import shuffle
from .alphabet import Alphabet


class Reflector:

    def __init__(self):
        self.alphabet = self.init_alphabet()

    @staticmethod
    def init_alphabet():
        alphabet = Alphabet()

        mixed_letters = list(alphabet.alphabet)
        shuffle(mixed_letters)

        alphabet_chars = {}
        for index, char in enumerate(alphabet.alphabet):
            alphabet_chars[char] = mixed_letters[index]

        return alphabet_chars

    def resolve_letter(self, letter):
        return self.alphabet[letter]

    def get_alphabet(self):
        return self.alphabet
