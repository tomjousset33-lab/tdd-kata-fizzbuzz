def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz representation of the integer n.

    Contract:
    - if n is a multiple of 3 AND 5: "FizzBuzz"
    - if n is a multiple of 3 only: "Fizz"
    - if n is a multiple of 5 only: "Buzz"
    - otherwise: str(n)

    Raises ValueError if n is not a strictly positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("fizzbuzz expects a strictly positive integer")

    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)
