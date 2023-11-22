def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y

from sympy import sqrt

def es_potencia(n, pot):
    return int((n)**(1/pot)) ** pot == n

def potencias_fibonacci(n, pot = 2):
    fibs = []
    a, b = 0, 1
    while a < n:
        if es_potencia(a, pot):
            fibs.append(a)
        a, b = b, a+b
    return fibs
