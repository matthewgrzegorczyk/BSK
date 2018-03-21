class Viegnere:
    """
    Viegnere cipher
    """
    def encode(self, plaintext: str, key: str) -> str:
        encoded = ''
        # Make the text uppercase.
        plaintext = plaintext.upper()
        key_index = 0
        key_len = len(key)

        for text_index in range(0, len(plaintext)):
            if text_index >= key_len:
                key_index = 0

            text_number = self.ascii_to_alpha_num(plaintext[text_index])
            key_number = self.ascii_to_alpha_num(key[key_index])

            encoded_alpha = (text_number + key_number) % 26
            encoded += self.alpha_num_to_ascii(encoded_alpha)
            key_index += 1

        return encoded

    def decode(self, encoded_text: str, key: str) -> str:
        decoded = ''
        # Make the text uppercase.
        encoded_text = encoded_text.upper()
        key_index = 0
        key_len = len(key)

        for text_index in range(0, len(encoded_text)):
            if text_index >= key_len:
                key_index = 0

            text_number = self.ascii_to_alpha_num(encoded_text[text_index])
            key_number = self.ascii_to_alpha_num(key[key_index])

            decoded_alpha = (text_number - key_number) % 26
            decoded += self.alpha_num_to_ascii(decoded_alpha)
            key_index += 1

        return decoded

    def ascii_to_alpha_num(self, char):
        return ord(char) - 65

    def alpha_num_to_ascii(self, number):
        return chr(number + 65)