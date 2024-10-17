#!/usr/bin/env python3
""" Basic Async Syntax
"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait random delay n times
    """
    tasks = [task_wait_random(max_delay) for task in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
