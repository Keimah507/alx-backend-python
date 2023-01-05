#!/usr/bin/env python3
"""Takes a list of floats and returns their sum as an integer"""
import math
from typing import List


def sum_list(input_list: [List[float]]) -> float:
    """returns sum of list of floats as an integer"""
    return math.fsum(input_list)
