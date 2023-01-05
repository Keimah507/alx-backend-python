#!/usr/bin/env python3
"""Checks element length in a list"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns element and its length in the list"""
    return [(i, len(i)) for i in lst]
