#!/usr/bin/env python3
""" Basic Async Syntax
"""


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio

def task_wait_random(max_delay: int) -> asyncio.Task:
    """ wait and return asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
