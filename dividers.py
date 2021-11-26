def dividers(value):
    return [number for number in range(1, number + 1) if value % number == 0]


print(dividers(21))
print(dividers(200))