from collections import deque


class LFSR:

    def __init__(self, taps, seed=''):
        self.taps = taps

        if not seed:
            seed = '1' + '0' * (max(self.taps) - 1)

        self.seed = deque(seed, len(seed))

    def next_int(self):
        first_tap = self.taps[0]
        input_val = int(self.seed[first_tap - 1])
        for tap in self.taps:
            if first_tap == tap:
                continue

            input_val ^= int(self.seed[tap - 1])

        self.seed.appendleft(str(input_val))
        return int(''.join(self.seed), 2)

    def next_int_ca(self):
        first_tap = self.taps[0]
        input_val = int(self.seed[first_tap - 1])
        for tap in self.taps:
            if first_tap == tap:
                continue

            input_val ^= int(self.seed[tap - 1])

        self.seed.appendleft(str(input_val))

    def get_input_bit(self):
        return self.seed[0]

    def get_last_bit(self):
        return self.seed[-1]

    def set_input_bit(self, bit):
        self.seed.popleft()
        self.seed.appendleft(bit)

