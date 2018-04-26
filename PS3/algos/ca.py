from .lfsr import LFSR


class CA:

    def __init__(self, taps, seed):
        self.lfsr = LFSR(taps, seed)

    def encrypt(self, text):
        encoded_text = ''

        for char in text:
            self.lfsr.next_int()
            next_bit = int(self.lfsr.next_int()) ^ ord(char)
            encoded_text += chr(next_bit)

        return encoded_text

    def decrypt(self, text):
        decoded_text = ''

        for char in text:
            self.lfsr.next_int()
            next_bit = int(self.lfsr.next_int()) ^ ord(char)
            decoded_text += chr(next_bit)

        return decoded_text
