def add(a: int, b: int):
    return a + b


def dev(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b