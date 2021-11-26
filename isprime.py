import math

def isPrime(n):
    for d in range(2, round(math.sqrt(n) + 1)):
        if (n % d == 0):
            return False
    return True

print(isPrime(9))
print(isPrime(7))
print(isPrime(27))
print(isPrime(83779279810803919409189301030718319038018031918083301839703180830103801037012791808308103017931800800180380819108083))