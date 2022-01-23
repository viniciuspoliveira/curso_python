def fb(n):
    if n % 5 == 0 and n % 3 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'

    return n

from random import randint
for i in range(100):
    aleatorio = randint(0, 250)
    print(fb(aleatorio))