import string

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
    print(e.rotors)
    input = 'MK'
    encoded = e.encode(input)
    print([x.shift for x in e.rotors])
    print('Input:', input, 'Encoded:', encoded)

    e.set_key('FLG')
    print([x.shift for x in e.rotors])
    print(e.encode(encoded))


def sample_enigma_init():
    e = Enigma('FLG')

    e.rotors[0].set_alphabet('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    e.rotors[1].set_alphabet('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    e.rotors[2].set_alphabet('BDFHJLCPRTXVZNYEIWGAKMUSQO')

    r = Reflector(e)
    r.set_alphabet('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    e.add_reflector(r)

    return e


def read_binary_files():
    files = [
        'enigma/files/test.bin',
        'enigma/files/test2.bin',
        'enigma/files/test3.bin'
    ]

    for file_name in files:
        file = open(file_name, 'rb')
        lines = file.readlines()
        print(file_name)
        for line in lines:
            output = ''
            for code in line:
                letter = chr(code)

                if letter in string.ascii_letters:
                    output += letter
            print(output)
        print()


if __name__ == '__main__':
    example()
    # read_binary_files()
