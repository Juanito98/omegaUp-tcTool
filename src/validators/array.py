from typing import Sequence


def eachElementBetween(A: Sequence[int], lo: int, hi: int) -> bool:
    for x in A:
        if x < lo or x > hi:
            return False
    return True
