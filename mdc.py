def mdc(a, b):
    r = a % b
    if r > 0:
        return mdc(b, r)
    return b


print(mdc(348, 156))
print(mdc(12, 6))