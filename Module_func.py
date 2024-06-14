import random


def add(a: str, b: str):
    a = (int(a, 2))
    b = (int(b, 2))
    return format(((a + b) % (2 ** 16)), '016b')


def multiplication(a: str, b: str):
    a = (int(a, 2))
    b = (int(b, 2))
    return format(((a * b) % ((2 ** 16) + 1)), '016b')


def xor(a: str, b: str, n: int):
    a = (int(a, 2))
    b = (int(b, 2))
    return format(a ^ b, f'0{n}b')


def cyclic_shift(k: str, shift: int):
    return k[shift:] + k[:shift]


def splitter(n: str, number: int):
    split = [(n[i:i + number]) for i in range(0, len(n), number)]
    return split



