def mdc(value1, value2):
    rest = value1 % value2
    if rest > 0:
        return mdc(value2, rest)
    return value2

print(mdc(150, 225))