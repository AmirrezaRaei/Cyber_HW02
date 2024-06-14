from Crypto import algorithm

if __name__ == '__main__':
    print("\ninput type :   \n1 - Decimal   \n2 - Binary   \n3 - Hex")

    input_type = int(input("Enter Type : "))

    print()

    plaintext = input("Enter Plain Text To Encrypt : ")
    key = input("Enter key Value : ")

    if input_type == 1:
        plaintext = format(plaintext, '128b')
        key = format(key, '064b')

    elif input_type == 2:
        plaintext = format((int(plaintext, 2)), '128b')
        key = format((int(key, 2)), '064b')

    elif input_type == 3:
        plaintext = format((int(plaintext[2:], 16)), '128b')
        key = format((int(key[2:], 16)), '064b')


    cipherText = algorithm(plaintext, key)
    cipherText = "{0:x}".format(int(cipherText, 2))
    print("\nCipher Text : " + "0x" + cipherText)
