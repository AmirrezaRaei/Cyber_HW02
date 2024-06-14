from Module_func import *


def IDEA_round(plaintext: str, key: str, nr: int, isLastRound: bool):
    plaintext = splitter(plaintext, 16)
    index = nr * 6

    # mode 1
    if not isLastRound:
        # step 1 : p1 * k1
        step_1 = multiplication(plaintext[0], key[index])
        # step 2 : p2 + k2
        step_2 = add(plaintext[1], key[index + 1])
        # step 3 : p3 * k3
        step_3 = multiplication(plaintext[2], key[index + 2])
        # step 4 : p4 + k4
        step_4 = add(plaintext[3], key[index + 3])
        # step 5 : XOR step 1 and step 3
        step_5 = xor(step_1, step_3, 16)
        # step 6 : XOR step 2 and step 4
        step_6 = xor(step_2, step_4, 16)
        # step 7 : step 5 * k5
        step_7 = multiplication(step_5, key[index + 4])
        # step 8 : step 7 + step 6
        step_8 = add(step_7, step_6)
        # step 9 : step 8 * step k6
        step_9 = multiplication(step_8, key[index + 5])
        # step 10 : step 7 + step 9
        step_10 = add(step_7, step_9)
        # step 11 : XOR step 1 and step 9
        step_11 = xor(step_1, step_9, 16)
        # step 12 : XOR step 3 and step 9
        step_12 = xor(step_3, step_9, 16)
        # step 13 : XOR step 2 and step 10
        step_13 = xor(step_2, step_10, 16)
        # step 14 : XOR step 4 and step 10
        step_14 = xor(step_4, step_10, 16)

        plaintext_round_result = f'{step_11}{step_12}{step_13}{step_14}'

    # mode2 (last round)
    else:
        # step 1 : R1 * k1
        step_1 = multiplication(plaintext[0], key[index])
        # step 2 : R2 + k2
        step_2 = add(plaintext[1], key[index + 1])
        # step 3 : R3 + k3
        step_3 = add(plaintext[2], key[index + 2])
        # step 4 : R4 * k4
        step_4 = multiplication(plaintext[3], key[index + 3])
        # plaintext_round_result = step_1 + " " + step_2 + " " + step_3 + " " + step_4 + " "
        plaintext_round_result = f'{step_1}{step_2}{step_3}{step_4}'

    return plaintext_round_result
