import string
from random import shuffle


class Rotor:

    def __init__(self, position):
        self.position = position.upper()
        self.basic_position = position.upper()
        self.alphabet = self.randomize_alphabet()

    def add_letter_mapping(self, letter_in, letter_out):
        letter_in = letter_in.upper()
        letter_out = letter_out.upper()
        index = string.ascii_uppercase.index(letter_in)
        self.alphabet[index] = letter_out

    def resolve_letter(self, letter):
        diff_alphabet = string.ascii_uppercase.index(letter.upper()) - string.ascii_uppercase.index('A')

        self.rotate()
        return self.alphabet[string.ascii_uppercase.index(self.position) + diff_alphabet]

    def randomize_alphabet(self):
        alphabet = list(string.ascii_uppercase)
        shuffle(alphabet)
        return alphabet

    def rotate(self):
        new_position = (string.ascii_uppercase.index(self.position) + 1) % len(string.ascii_uppercase)
        self.position = string.ascii_uppercase[new_position]

    def is_full_rotate(self):
        return self.position == self.basic_position
