class Enigma:
    rotors = []

    def add_rotor(self, rotor):
        self.rotors.append(rotor)
        
    def encode(self):
        pass

    def decode(self):
        pass


class Rotor:
    letter_map = {}

    def __init__(self, map):
        self.letter_map = map

    def add_letter_mapping(self, letter_in, letter_out):
        self.letter_map[letter_in] = letter_out

    def map_letter(self, letter):
        self.letter_map.get(letter, '')
