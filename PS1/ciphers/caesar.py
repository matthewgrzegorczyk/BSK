class Caesar:
    """
    Caesar cipher
    """
    first_char_code = 65
    last_char_code = 90
    alphabet_size = last_char_code - first_char_code + 1

    def __init__(self, shift=3):
        self.shift = shift
    
    def encode(self, plaintext: str) -> str:
        encoded = ''
        # Make the text uppercase.
        plaintext = plaintext.upper()

        for letter in plaintext:
            shifted_letter_code = ((ord(letter) - self.first_char_code + self.shift) % self.alphabet_size) + self.first_char_code
            print("{} ({}) => {} ({})".format(letter, ord(letter), chr(shifted_letter_code), shifted_letter_code))
            encoded = encoded + chr(shifted_letter_code)

        return encoded

    def decode(self, encoded_phrase: str) -> str:
        decoded = ''

        for letter in encoded_phrase:
            shifted_letter_code = ((ord(letter) - self.first_char_code - self.shift) % self.alphabet_size) + self.first_char_code
            decoded = decoded + chr(shifted_letter_code)

        return decoded