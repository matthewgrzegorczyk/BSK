from typing import List


class RailFence:
    """
    Rail Fence cipher
    """

    def __init__(self, key=3):
        self.key = key

    def set_key(self, key):
        self.key = key

    def encode(self, plaintext: str) -> str:
        zigzag = self.build_zigzag(plaintext)
        self.zigzag = zigzag
        cipher = ''
        for row in zigzag:
            cipher = cipher + ''.join(row)

        return cipher

    def decode(self, encoded_text: str) -> str:
        zigzag = self.rebuild_zigzag2(encoded_text)
        decoded = self.read_zigzag(zigzag)

        return decoded

    def build_zigzag(self, plaintext: str) -> str:
        level = 0
        zigzag = []
        for letter in plaintext:
            if level == self.key - 1:
                direction = -1
            elif level == 0:
                direction = 1

            try:
                zigzag[level].append(letter)
            except IndexError:
                zigzag.append([])
                zigzag[level].append(letter)

            level = level + direction

        return zigzag

    def rebuild_zigzag(self, encoded_text: str) -> List:
        level = 0
        top_row = 0
        zigzag = []
        letter_list = list(encoded_text)
        selected_list = 0
        for top_row in range(self.key):
            for letter in encoded_text:
                if level == self.key - 1:
                    direction = -1
                elif level <= top_row:
                    direction = 1

                if top_row == level and letter_list:
                    try:
                        zigzag[selected_list].append(letter_list.pop(0))
                    except IndexError:
                        zigzag.append([])
                        zigzag[selected_list].append(letter_list.pop(0))
                    if selected_list < self.key - 1:
                        selected_list = selected_list + 1
                    else:
                        selected_list = selected_list - 1

                level = level + direction

        return zigzag

    def rebuild_zigzag2(self, encoded_text):
        helper = 0
        direction = 1
        letter_list = list(encoded_text)
        text_length = len(encoded_text)
        zigzag = []

        for index in range(self.key):
            helper = 0
            for i, letter in enumerate(encoded_text):
                if not letter_list:
                    break

                if index == helper and i in range(index, text_length + 1):
                    try:
                        zigzag[index]
                        zigzag[index].append(letter_list.pop(0))
                    except IndexError:
                        zigzag.append([])
                        zigzag[index].append(letter_list.pop(0))

                if helper >= self.key - 1:
                    direction = -1
                elif helper <= 0:
                    direction = 1

                helper += direction

        return zigzag

    def read_zigzag(self, zigzag: List, ) -> str:
        level = 0
        output = ''
        zigzag_length = sum(len(row) for row in zigzag)

        for x in range(zigzag_length):
            if level == self.key - 1:
                direction = -1
            elif level == 0:
                direction = 1

            if zigzag[level]:
                output = output + zigzag[level].pop(0)

            level = level + direction

        return output
