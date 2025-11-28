from math import isqrt
import random

class InvalidInputError(Exception):
    pass


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_of_primes(numbers: list[int]) -> int:

    if not isinstance(numbers, list):
        raise InvalidInputError("El parámetro debe ser una lista de enteros.")

    if not numbers:
        return 0

    total = 0
    for idx, value in enumerate(numbers):
        if not isinstance(value, int):
            raise InvalidInputError(
                f"Se esperaba un entero en índice {idx}. Valor recibido: {value!r}"
            )
        if value >= 2 and is_prime(value):
            total += value

    return total


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # OJO: esto con is_prime() es lentísimo para 100_000_000 elementos
    data2 = [random.randint(1, 100_000_000) for _ in range(100_000)]
    print(sum_of_primes(data))
    print(sum_of_primes(data2))
