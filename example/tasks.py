import time
import random


def multiply(x, y):
    return x * y


def buggy():
    raise Exception('oops')
    return None
