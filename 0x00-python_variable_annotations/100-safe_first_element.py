#!/usr/bin/env python3
"""Return first element in a list"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element in a list"""
    if lst:
        return lst[0]
    else:
        return None
