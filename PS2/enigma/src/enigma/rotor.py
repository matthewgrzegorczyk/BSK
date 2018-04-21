class Rotor:
    shift = 0
    rotate_count = 0

    def __init__(self, enigma, shift=0):
        self.shift = shift
        self.enigma = enigma
        self.base_alphabet = list(enigma.alphabet)
        self.alphabet = list(enigma.alphabet)

    def set_alphabet(self, alphabet):
        if len(alphabet) == len(self.base_alphabet):
            self.alphabet = list(alphabet)

    def set_shift_by_letter(self, letter):
        self.shift = self.base_alphabet.index(letter)

    def get_index(self, index):
        return (index + self.shift) % len(self.base_alphabet)

    def rotate(self):
        self.shift += 1
        self.rotate_count = (self.rotate_count + 1) % len(self.base_alphabet)

        return self.rotate_count == 0

    def encode(self, letter, direction=1, prev_shift=0):
        print(letter, direction, prev_shift)
        if direction == 1:
            index = self.get_index(self.base_alphabet.index(letter) - prev_shift)
            return self.alphabet[index]
        elif direction == -1:
            index = self.get_index(self.base_alphabet.index(letter) + prev_shift)
            # print('prev_shift', prev_shift, 'index', index, 'shift', self.shift
            return self.base_alphabet[index]
