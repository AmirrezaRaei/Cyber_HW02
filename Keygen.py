from Module_func import splitter, cyclic_shift


def keygen(key):
    keys = []
    for i in range(8):
        temp = splitter(key, 16)
        keys.extend(temp[0:8])
        cyclic_shift(key, 25)

    return keys
