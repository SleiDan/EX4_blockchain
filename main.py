def encrypt(etext, k):
    return pow(etext, k[1], k[0])


def decrypt(dtext, key):
    return pow(dtext, key[1], key[0])


def split(text):
    res = []
    for i in text:
        res.append(ord(i))
    return res


def div(a, b):
    if b != 0:
        x1, y1 = div(b, a % b)
        x = y1
        y = x1 - int(a / b) * y1
        return x, y
    else:
        x = 1
        y = 0
        return x, y


def gen_the_Key():
    q = 1109
    p = 1103
    e = 65537
    n = q * p
    fn = (q - 1) * (p - 1)
    x, y = div(e, fn)
    if x < 0:
        x = x + fn
    d = x
    return (n, e), (n, d)


def eText(inp, k1):
    inp = split(inp)
    result = []
    code = []
    for i in inp:
        t = 0
        i = int(i)
        if t != 0:
            result.append((i + result[t - 1]) % 123)
        else:
            result.append(i)
        t += 1
    for i in result:
        code.append(encrypt(i, k1))
    return code

def dText(etext, k2):
    result = []
    message = ''
    for i in etext:
        t = 0
        i = int(i)
        if t == 0:
            result.append(i)
        else:
            result.append((i - result[t-1])%123)
        t += 1
    for i in result:
        message += chr(decrypt(i, k2))
    return message


k1, k2 = gen_the_Key()
print('Введите то, что хотите зашифровать:')
inp = input()
etext = eText(inp, k1)
dtext = dText(etext, k2)
print('Зашифрованный текст:')
print(etext)
print('Расшифрованный текст:')
print(dtext)