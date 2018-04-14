import string
from rotor import Rotor

def read_rotors():
    rotors = []
    with open('rotors.txt', 'r') as f_rotors:
        lines = f_rotors.readlines()

        for line in lines:
            line = line.strip() # Remove any whitespace
            
            rotor = Rotor()
            rotor.set_alphabet(line)
            rotors.append(rotor)

    return rotors

def test_rotors():
    rotors = read_rotors()
    key = 'FLG'

    i = 0
    for k in reversed(key):
        rotors[i].set_shift_by_letter(k)
        i += 1

    input_string = 's'
    for input_letter in input_string:
        rotors[0].rotate()
        idx = 0
        for rotor in rotors:
            letter = rotor.get_letter_by_input_letter_index(input_letter)
            idx -= string.ascii_uppercase.index(letter) 
            input_letter = rotor.get_letter_by_alphabet_index(idx)

            print(letter, idx, input_letter)

    return rotors


