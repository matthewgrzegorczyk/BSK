ALPHABET_COUNT = 256


class Alphabet:

    def __init__(self):
        self.alphabet = self.generate_alphabet()

    @staticmethod
    def generate_alphabet(length=ALPHABET_COUNT):
        alphabet = []

        for i in range(length):
            alphabet.append(chr(i))

        return alphabet

    def get_alphabet(self):
        return self.alphabet
