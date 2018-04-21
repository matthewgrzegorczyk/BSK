class Reflector:
    shift = 0

    def __init__(self, enigma):
        self.enigma = enigma
        self.base_alphabet = enigma.alphabet
        self.alphabet = enigma.alphabet

    def set_shift(self, shift):
        self.shift = shift

    def set_alphabet(self, alphabet):
        if len(alphabet) == len(self.base_alphabet):
            self.alphabet = list(alphabet)

    def get_index(self, index):
        return (index + self.shift) % len(self.base_alphabet)

    def encode(self, letter, prev):
        prev_shift = getattr(prev, 'shift', 0)
        index = self.get_index(self.base_alphabet.index(letter) - prev_shift)
        return self.alphabet[index]
