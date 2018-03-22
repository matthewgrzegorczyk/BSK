from math import ceil

class Matrix:
    """
    Matrix cipher
    """

    def __init__(self, key: str):
        self.key_dict = self.prepare_key_dict(key)
        self.period = len(self.key_dict)

    def encode(self, plaintext: str) -> str:
        encoded = ''
        plaintext = plaintext.upper()
        plaintext_len = len(plaintext)
        rows = int(ceil(plaintext_len / self.period))

        for row_index in range(0, rows):
            for key_index, key_value in self.key_dict.items():
                pos = int(key_value) + (row_index * self.period) - 1
                if pos >= plaintext_len:
                    encoded += '%'
                else:
                    encoded += plaintext[pos]

        return encoded

    def decode(self, encoded_phrase: str) -> str:
        decoded = ''
        encoded = encoded_phrase.upper()
        encoded_len = len(encoded_phrase)
        rows = (int(ceil(encoded_len / self.period)))
        inversed_key = self.inverse_key_dict()

        for row_index in range(0, rows):
            for key_index, key_value in inversed_key.items():
                pos = int(key_value) + (row_index * self.period)
                decoded += encoded[pos]

        return self.clean_from_special(decoded)

    def prepare_key_dict(self, key: str) -> dict:
        splitted_key = key.split('-')
        key_dict = {}

        for index, column in enumerate(splitted_key):
            key_dict[int(index)] = int(column)

        return key_dict

    def inverse_key_dict(self) -> dict:
        key_dict = {}
        for index, column in self.key_dict.items():
            key_dict[int(column)] = int(index)

        return dict(sorted(key_dict.items()))

    def clean_from_special(self, encoded_text: str) -> str:
        return encoded_text.replace("%", "")

