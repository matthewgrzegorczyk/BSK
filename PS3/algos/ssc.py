from PS3.algos.lfsr import LFSR


class SSC:

    def __init__(self, taps, seed):
        self.lfsr = LFSR(taps, seed)

    def crypt(self, text):
        coded_text = ''

        for char in text:
            self.lfsr.next_int()
            coded_text += chr(ord(char) ^ (int(self.lfsr.get_input_bit()) + int(self.lfsr.get_last_bit())))

        return coded_text


ssc_enc = SSC([9, 5, 3, 1], '100101011')
ssc_dec = SSC([9, 5, 3, 1], '100101011')

plain_text = 'ALFA_ROMEO'
encoded_text = ssc_enc.crypt(plain_text)
decoded_text = ssc_dec.crypt(encoded_text)

print('Plain text: {}'.format(plain_text))
print('Encoded text: {}'.format(encoded_text))
print('Decoded text: {}'.format(decoded_text))