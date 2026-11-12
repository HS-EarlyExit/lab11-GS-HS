import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be zero")
    return b / a

def log(a, b):
    # log base a of b
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("a and b must be positive and a cannot equal 1")
    return math.log(b, a)

def exp(a, b):
    return a ** b
