"""
Funciones de uso general
"""


def isPalindromo(cad: str) -> bool:
    return cad == cad[::-1]


def fact(n):
    # n! = n * (n-1)!
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    for i in range(100):
        print(fib(i), end=" ")
    # print()
    # print(isPalindromo("ana"))
    # print(isPalindromo("hola"))
    # print(fact(998))
