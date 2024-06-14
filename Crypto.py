from Keygen import keygen
from Module_func import splitter, xor, cyclic_shift
from F_function import fBox


def algorithm(plaintext: str, key: str):
    split_plaintext = plaintext
    target_key = key
    for i in range(0, 8):
        split_plaintext = splitter(split_plaintext, 64)
        left = split_plaintext[0]
        right = split_plaintext[1]

        split_key = splitter(target_key, 64)
        left_key = cyclic_shift(split_key[0], 72)
        right_key = cyclic_shift(split_key[1], 62)

        target_key = keygen(target_key)

        result_fBox = fBox(right, target_key)
        left = xor(result_fBox, left, 64)

        target_key = left_key + right_key
        split_plaintext = right + left

    return split_plaintext
