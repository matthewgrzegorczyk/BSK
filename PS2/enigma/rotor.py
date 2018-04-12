import string
from random import shuffle


class Rotor:
    alphabet = list(string.ascii_uppercase)

    def __init__(self, shift=0):
        self.shift = shift

    def add_letter_mapping(self, letter_in, letter_out):
        letter_in = letter_in.upper()
        letter_out = letter_out.upper()
        index = string.ascii_uppercase.index(letter_in)
        self.alphabet[index] = letter_out

    def resolve_letter(self, letter):
        letter = letter.upper()
        index = string.ascii_uppercase.index(letter)

        return self.alphabet[index]

    def index(self, idx):
        return self.shift + idx % len(self.alphabet)

    def get_letter_by_index(self, idx):
        index = self.index(idx)

        return self.alphabet[index]

    def get_letter_by_base_letter(self, letter):
        letter = letter.upper()
        idx = string.ascii_uppercase.index(letter)

        return self.alphabet[idx]

    def randomize_alphabet(self):
        self.alphabet = list(string.ascii_uppercase)
        shuffle(self.alphabet)

    def set_alphabet(self, alphabet):
        if (len(alphabet) == 26):
            self.alphabet = list(alphabet)

    def rotate(self, direction=1):
        # if direction == 1:
        #     self.alphabet = self.alphabet[-1:] + self.alphabet[:-1]
        # elif direction == -1:
        #     self.alphabet = self.alphabet

        self.shift += direction
