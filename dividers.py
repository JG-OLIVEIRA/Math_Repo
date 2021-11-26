def dividers(n):
    return [d for d in range(1, n + 1) if n % d == 0]


print(dividers(21))
print(dividers(200))