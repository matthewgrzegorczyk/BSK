from enigma.enigma import Enigma


def example():
    print('Example ...')
    e = Enigma('FLH')

    e.elements[0].set_alphabet('AJDKSIRUXBLHWTMCQGZNPYFVOE')
    # e.elements[0].rotate()
    letter = 'A'
    print(letter, ' => ', e.elements[0].encode(letter))
    # e.elements[1].set_alphabet('EKMFLGDQVZNTOWYHXUSPAIBRCJ')
    # e.elements[2].set_alphabet('BDFHJLCPRTXVZNYEIWGAKMUSQO')
    #
    # e.encode('S')


def read_binary_files():
    file1 = open('files/test.bin')


if __name__ == '__main__':
    example()
