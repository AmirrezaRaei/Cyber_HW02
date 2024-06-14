from F_round import IDEA_round
from Module_func import splitter


def fBox(plaintext: str, key: str):  # idea function

    ciphertext = plaintext
    for r in range(9):
        # print("--------------- " + "round : " + str(r + 1) + " ---------------")
        ciphertext = IDEA_round(ciphertext, key, r, (r + 1) % 9 == 0)

    return ciphertext
