import time
import asyncio
import numpy as np
from array import array


def add(a, b):
    return float(a + b)


def is_even(a):
    return a % 2 == 0


def is_true(a):
    return a == True


def hello():
    return "Hello world!"


def str_len(str):
    return float(len(str))


def str_join(s1, s2):
    return s1 + s2


def get_max(buf):
    nums = array("h")
    # The buf is a Uint8 array and we need to view it as a Uint16 array
    # The 'h' type code means viewing the buf as a Uint16 array
    # Learn about the type codes here https://docs.python.org/3/library/array.html#module-array
    nums.frombytes(buf)
    max = 0
    for x in nums:
        if x > max:
            max = x
    return float(max)


def get_min(buf):
    # We don't need to use the array function because the data has been passed as a Uint8 array
    return float(np.min(buf))

def prime_numbers(n):
    result = array("h")
    for num in range(0, int(n)):
        if is_prime(num):
            result.append(num)
    return memoryview(result.tobytes())


def is_prime(a):
    if a > 1:
        for num in range(2, int(a**0.5) + 1):
            if a % num == 0:
                return False
        return True
    return False


async def sleep():
    time.sleep(0.1)

def sum(buf):
    return asyncio.run(sum_async(buf))

async def sum_async(buf):
    total = 0
    for num in buf:
        await sleep()
        total += num
    return float(total)
