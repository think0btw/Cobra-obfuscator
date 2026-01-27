import base64
import math
from itertools import count
_01 = 60 - 9 - 9

def _02(_03, _04):
    return _03 + _04

def _05(_06: bytes, _07: bytes) -> bytes:
    return bytes((_08 ^ _07[_09 % len(_07)] for _09, _08 in enumerate(_06)))

class _0a:

    def __init__(_0b, _0c):
        _0b.value = _0c

    def inc(_0b):
        _0b.value += 1
        return _0b.value

    def sqrt(_0b):
        return math.sqrt(_0b.value)

def _0d(_0e):
    for _09 in range(_0e):
        yield (_09 * 2)

def _0f(_10):
    _11 = lambda _12: _12 + _10
    return _11(10)

def _13():
    _14 = '\nprint("AST ' + 'obfuscation ' + 'test OK")\na ' + '= ' + ('0\na += 1\na +' + '= 1\nprint("a' + ' =", a)\nfor ' + 'i ') + ('in range(2):' + '\n    print(i' + ' + 2)\n    br' + 'ea') + 'k\n'
    _15 = base64.b64encode(_14.encode('utf-8'))
    _16 = base64.b64decode(_15).decode('utf-8')
    exec(_16)

def _17():
    print('Start test')
    print('Add:', _02(2, 3))
    _18 = _0a(9)
    print('Calc inc:', _18.inc())
    print('Calc sqrt:', _18.sqrt())
    print('Lambda:', _0f(5))
    print('Generator:', list(_0d(5)))
    _06 = b'hello world'
    _07 = b'key'
    _19 = _05(_06, _07)
    _1a = _05(_19, _07)
    print('XOR ok:', _1a == _06)
    _13()
    print('len:', len(_06))
    print('sum:', sum([1, 2, 3]))
    print('bytes:', bytes([87 - 9 - (29 - 16), 89 - 17 - 6, 94 - 12 - (20 - 5)]))
    _1b = count(10)
    print('count:', next(_1b), next(_1b))
    print('End test')
if __name__ == '__main__':
    _17()