import string
from random import shuffle
from .alphabet import Alphabet
from .alphabet import ALPHABET_COUNT


class Rotor:
    alphabet = []
    alphabet_class = Alphabet()
    rotate_count = 0

    def __init__(self, shift=0):
        self.shift = shift
        self.alphabet = list(self.alphabet_class.alphabet)

    def add_letter_mapping(self, letter_in, letter_out):
        index = self.alphabet_class.alphabet.index(letter_in)
        self.alphabet[index] = letter_out

    def randomize_alphabet(self):
        self.alphabet = list(self.alphabet_class.alphabet)
        shuffle(self.alphabet)

    def set_alphabet(self, alphabet):
        if len(alphabet) == ALPHABET_COUNT:
            self.alphabet = list(alphabet)

    def index(self, idx):
        return (self.shift + idx) % len(self.alphabet)

    def get_letter_by_input_letter_index(self, letter):
        """Gets letter by input letter index, where letter is char in range 0x00 - 0xFF"""
        letter = letter.upper()
        return self.get_letter_by_alphabet_index(self.alphabet_class.alphabet.index(letter))

    def get_letter_by_alphabet_index(self, idx):
        """Gets letter by base alphabet index, where idx is number in range(0, 255)"""
        index = self.index(idx)

        return self.alphabet[index]

    def get_letter_by_base_letter(self, letter):
        """Gets alphabet letter by base letter."""
        letter = letter.upper()
        idx = self.alphabet_class.alphabet.index(letter)

        return self.alphabet[idx]

    def rotate(self, direction=1):
        # if direction == 1:
        #     self.alphabet = self.alphabet[-1:] + self.alphabet[:-1]
        # elif direction == -1:
        #     self.alphabet = self.alphabet

        self.shift += direction
        self.rotate_count += 1

    def set_shift_by_letter(self, letter):
        idx = self.alphabet_class.alphabet.index(letter)

        self.shift = idx

    def is_full_cycle(self):
        return self.rotate_count >= ALPHABET_COUNT

    def swap_alphabets(self):
        a = self.alphabet
        self.alphabet = self.alphabet_class.alphabet
        self.alphabet_class.alphabet = a
