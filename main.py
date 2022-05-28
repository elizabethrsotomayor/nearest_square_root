import math


def nearest_sq(n: int) -> int:
    """
    Returns the nearest square root of a given number.
    :param n:
    :return:
    """
    sq = math.sqrt(n)
    nearest = math.pow(round(sq), 2)
    return nearest
