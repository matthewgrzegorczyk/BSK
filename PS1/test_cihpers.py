import unittest

from ciphers.caesar import Caesar
from ciphers.rail_fence import RailFence
from ciphers.viegnere import Viegnere
from ciphers.matrix import Matrix


class TestCipherMethods(unittest.TestCase):
    phrase = 'CRYPTOGRAPHY'

    def test_caesar(self):
        caesar = Caesar()
        encoded_phrase = caesar.encode(self.phrase)
        decoded_phrase = caesar.decode(encoded_phrase)
        print('{0} => {1} => {2}'.format(self.phrase, encoded_phrase, decoded_phrase))

        self.assertEqual(decoded_phrase, self.phrase)

    def test_rail_fence(self):
        rail_fence = RailFence()
        encoded_phrase = rail_fence.encode(self.phrase)
        decoded_phrase = rail_fence.decode(encoded_phrase)
        print('{0} => {1} => {2}'.format(self.phrase, encoded_phrase, decoded_phrase))

        self.assertEqual(decoded_phrase, self.phrase)

    def test_viegnere(self):
        key = 'BREAKBREAKBR'
        viegnere = Viegnere()
        encoded_phrase = viegnere.encode(self.phrase, key)
        decoded_phrase = viegnere.decode(encoded_phrase, key)
        print('{0} => {1} => {2}'.format(self.phrase, encoded_phrase, decoded_phrase))

        self.assertEqual(decoded_phrase, self.phrase)

    def test_matrix(self):
        key = '3-4-1-5-2'
        matrix = Matrix(key)
        encoded_phrase = matrix.encode(self.phrase)
        decoded_phrase = matrix.decode(encoded_phrase)
        print('{0} => {1} => {2}'.format(self.phrase, matrix.clean_from_special(encoded_phrase), decoded_phrase))

        self.assertEqual(decoded_phrase, self.phrase)

if __name__ == '__main__':
    unittest.main()