#!/usr/bin/env python3
""" Basic Async Syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that waits for a random delay
    @max_delay: an integer represent max delay

    Return: random float value
    """
    randNum = random.uniform(0, max_delay)
    await asyncio.sleep(randNum)
    return randNum
