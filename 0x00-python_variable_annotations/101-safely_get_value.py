#!/usr/bin/env python3
"""Refactoring code to add type annotations"""
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Checks if key exists in dictonary"""
    if key in dct:
        return dct[key]
    else:
        return default
