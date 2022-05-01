"""
Simple Calculator Controller
"""

def add(a: int, b: int):
    return a + b

def subtract(a: int, b: int):
    return a - b

def multiply(a: int, b: int):
    return a * b

def divide(a: int, b: int):
    return a / b


if __name__ == '__main__':
    from controller import log
    log.info('default logger log...')