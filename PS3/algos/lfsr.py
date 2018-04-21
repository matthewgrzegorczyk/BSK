from collections import deque


class LFSR:

    def __init__(self, taps, seed=''):
        self.taps = taps

        if not seed:
            seed = '1' + '0' * (max(self.taps) - 1)

        self.seed = deque(seed, len(seed))

    def next_int(self):
        input_val = 0
        for tap in self.taps:
            input_val ^= int(self.seed[tap - 1])

        self.seed.appendleft(str(input_val))
        return int(''.join(self.seed), 2)

    def get_input_bit(self):
        return self.seed[0]

    def get_last_bit(self):
        return self.seed[-1]

    def set_input_bit(self, bit):
        self.seed.popleft()
        self.seed.appendleft(bit)
