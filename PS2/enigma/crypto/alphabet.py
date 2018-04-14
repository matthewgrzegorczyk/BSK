import string

ALPHABET_COUNT = 26


class Alphabet:

    def __init__(self):
        self.alphabet = string.ascii_uppercase

    @staticmethod
    def generate_alphabet(length=ALPHABET_COUNT):
        alphabet = []

        for i in range(length):
            alphabet.append(chr(i))

        return alphabet

    def set_ascii_alphabet(self):
        self.alphabet = string.ascii_uppercase
