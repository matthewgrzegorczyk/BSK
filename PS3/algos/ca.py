from PS3.algos.lfsr import LFSR


class CA:

    def __init__(self, taps, seed):
        self.lfsr = LFSR(taps, seed)

    def encrypt(self, text):
        encoded_text = ''

        for char in text:
            self.lfsr.next_int()
            next_bit = int(self.lfsr.get_input_bit()) ^ ord(char)
            self.lfsr.set_input_bit(str(next_bit))
            encoded_text += chr(next_bit)

        return encoded_text

    def decrypt(self, text):
        decoded_text = ''

        for char in text:
            self.lfsr.next_int()
            next_bit = int(self.lfsr.get_input_bit()) ^ ord(char)
            self.lfsr.set_input_bit(str(next_bit))
            decoded_text += chr(next_bit)

        return decoded_text


ca_enc = CA([7, 5, 3, 1], '101100101')
ca_dec = CA([7, 5, 3, 1], '101100101')

encoded = ca_enc.encrypt('ALFA_ROMEO')
decoded = ca_dec.decrypt(encoded)
print('Encoded: {}'.format(encoded))
print('Decrypted: {}'.format(decoded))
