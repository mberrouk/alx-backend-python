#!/usr/bin/env python3
""" Async Generator """


import random
import asyncio


async def async_generator():
    """ Async generator example 
    """
    asyncio.sleep(1)
    yield random.randrange(10)
