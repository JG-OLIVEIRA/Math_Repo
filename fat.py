def fat(value):
    if value > 1:
        return value * fat(value - 1)
    return 1



print(fat(5)/ fat(3) * fat(2))
print(fat(4))
print(fat(3))
print(fat(2))
print(fat(1))