#!/usr/bin/env python3
"""takes a list of integers and floats and returns their sum as a float"""
import math
from typing import Union, List


def sum_mixed_list(mxd_list: [List[Union[int, float]]]) -> float:
    """Returns sum of mxd list as a float"""
    return math.fsum(mxd_list)
