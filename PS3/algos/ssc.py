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