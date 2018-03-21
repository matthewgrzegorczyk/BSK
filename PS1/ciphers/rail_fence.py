class RailFence:
    """
    Rail Fence cipher
    """

    def __init__(self, key=3):
        self.key = key

    def encode(self, plaintext: str) -> str:
        cipher_levels = []
        level = 0
        direction = 1

        for letter in plaintext:
            if level == self.key - 1:
                direction = -1
            elif level == 0:
                direction = 1

            try:
                cipher_levels[level].append(letter)
            except IndexError:
                cipher_levels.append([])
                cipher_levels[level].append(letter)

            level = level + direction
        cipher = ''
        for cipher_level in cipher_levels:
            cipher = cipher + ''.join(cipher_level)

        return cipher

    def decode(self, encoded_text: str) -> str:
        decoded = ''
        return decoded
