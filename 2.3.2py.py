import itertools
import math

def primes():
    number = 1
    while True:
        number += 1
        if (math.factorial(number - 1) + 1) % number == 0:
            yield number


print(list(itertools.takewhile(lambda x: x <= 1000, primes())))