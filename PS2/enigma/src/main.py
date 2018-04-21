from enigma.enigma import Enigma
from enigma.reflector import Reflector


def example():
    print('Example ...')
    e = Enigma('FLG')

    e.rotors[0].set_alphabet('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    e.rotors[1].set_alphabet('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    e.rotors[2].set_alphabet('BDFHJLCPRTXVZNYEIWGAKMUSQO')

    r = Reflector(e)
    r.set_alphabet('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    e.add_reflector(r)
    print('Input: S', 'Output:', e.encode('S'))


def read_binary_files():
    file1 = open('files/test.bin')


if __name__ == '__main__':
    example()
