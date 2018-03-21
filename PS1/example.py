from ciphers.caesar import Caesar
from ciphers.rail_fence import RailFence

if __name__ == '__main__':
    phrase = 'CRYPTOGRAPHY'
    caesar = Caesar(shift=3)
    encoded_phrase = caesar.encode(phrase)
    decoded_phrase = caesar.decode(encoded_phrase)

    rail_fence = RailFence(key=3)
    rf_encoded_phrase = rail_fence.encode(phrase)
    rf_decoded_phrase = rail_fence.decode(rf_encoded_phrase)
    print()
    print("Phrase: " + phrase)
    print()
    print("####### Caesar cipher #######")
    print("Encoded phrase: " + encoded_phrase)
    print("Decoded phrase: " + decoded_phrase)
    print("#############################")
    print()
    print("####### Rail Fence cipher #######")
    print("Encoded phrase: " + rf_encoded_phrase)
    print("Decoded phrase: " + rf_decoded_phrase)
    print("#################################")