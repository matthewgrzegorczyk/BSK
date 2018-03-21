import unittest

from ciphers.caesar import Caesar
from ciphers.rail_fence import RailFence


class TestCipherMethods(unittest.TestCase):
    phrase = 'CRYPTOGRAPHY'

    def test_caesar(self):
        caesar = Caesar()
        encoded_phrase = caesar.encode(self.phrase)
        decoded_phrase = caesar.decode(encoded_phrase)

        self.assertEqual(decoded_phrase, self.phrase)

    def test_rail_fence(self):
        rail_fence = RailFence()
        encoded_phrase = rail_fence.encode(self.phrase)
        decoded_phrase = rail_fence.decode(encoded_phrase)
        print(encoded_phrase)
        

        self.assertEqual(decoded_phrase, self.phrase)

if __name__ == '__main__':
    unittest.main()