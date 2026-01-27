import base64
import math
from itertools import count

CONSTANT = 42


def add(a, b):
    return a + b


def crypto_xor(data: bytes, key: bytes) -> bytes:
    return bytes(
        (byte ^ key[i % len(key)]) for i, byte in enumerate(data)
    )


class Calculator:
    def __init__(self, value):
        self.value = value

    def inc(self):
        self.value += 1
        return self.value

    def sqrt(self):
        return math.sqrt(self.value)


def generator_test(n):
    for i in range(n):
        yield i * 2


def lambda_test(x):
    f = lambda y: y + x
    return f(10)


def base64_exec_test():
    payload = """
print("AST obfuscation test OK")
a = 0
a += 1
a += 1
print("a =", a)
for i in range(2):
    print(i + 2)
    break
"""
    encoded = base64.b64encode(payload.encode("utf-8"))
    decoded = base64.b64decode(encoded).decode("utf-8")
    exec(decoded)


def main():
    print("Start test")

    print("Add:", add(2, 3))

    calc = Calculator(9)
    print("Calc inc:", calc.inc())
    print("Calc sqrt:", calc.sqrt())

    print("Lambda:", lambda_test(5))

    print("Generator:", list(generator_test(5)))

    data = b"hello world"
    key = b"key"
    encrypted = crypto_xor(data, key)
    decrypted = crypto_xor(encrypted, key)

    print("XOR ok:", decrypted == data)

    base64_exec_test()

    # builtin stress
    print("len:", len(data))
    print("sum:", sum([1, 2, 3]))
    print("bytes:", bytes([65, 66, 67]))

    # itertools
    c = count(10)
    print("count:", next(c), next(c))

    print("End test")


if __name__ == "__main__":
    main()


