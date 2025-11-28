from math import isqrt
import random

class InvalidInputError(Exception):
    pass


#metodo Criba de Eratostenes
def criba(max_val: int) -> list[bool]:

    primes = bytearray(b"\x01") * (max_val + 1)
    primes[0] = primes[1] = False

    limit = isqrt(max_val)

    for i in range(2, limit + 1):
        if primes[i]:
            start = i * i
            primes[start:max_val + 1:i] = [False] * ((max_val - start) // i + 1)

    return primes


def sum_of_primes(numbers: list[int]) -> int:

    if not isinstance(numbers, list):
        raise InvalidInputError("El parámetro debe ser una lista de enteros.")

    if not numbers:
        return 0

    max_val = 0
    for idx, value in enumerate(numbers):
        if not isinstance(value, int):
            raise InvalidInputError(
                f"Se esperaba un entero en índice {idx}. Valor recibido: {value!r}"
            )
        if value > max_val:
            max_val = value

    if max_val < 2:
        return 0

    primes = criba(max_val)

    total = 0
    for num in numbers:
        if primes[num]:
            total += num

    return total


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data2 = [random.randint(1, 100_000_000) for _ in range(100_000_000)]
    print(sum_of_primes(data))
    print(sum_of_primes(data2))
