#!/usr/bin/env python3
"""Python Async comprehension task 1"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers and returns them"""
    randnums = [i async for i in async_generator()]
    return randnums
