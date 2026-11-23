from math import sqrt


def solve(a: float, b: float, c: float) -> tuple[list[float], bool]:
    """Return the real roots of ax**2 + bx + c = 0 and whether any exist.

    With a == 0, solve a linear equation, return no roots for a nonzero
    constant, or raise ValueError for the identity 0 = 0. For a quadratic,
    a zero discriminant gives one root and a negative one gives none.
    """
    if a == 0:
        if b != 0:
            return [-c / b], True
        if c != 0:
            return [], False
        raise ValueError("The identity 0 = 0 has infinitely many solutions.")

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return [], False

    denominator = 2 * a
    if discriminant == 0:
        return [-b / denominator], True

    square_root = sqrt(discriminant)
    return [(-b + square_root) / denominator, (-b - square_root) / denominator], True
