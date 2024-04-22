#!/usr/bin/env python3
"task 0 module"
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    "waits for an amound of seconds"
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
