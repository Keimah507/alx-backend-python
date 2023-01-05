#!/usr/bin/env python3
"""Takes float multiplier as an argument and returns a function
that multiplies float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies float by multiplier"""
    def mult(m):
        return m * multiplier
    return mult
