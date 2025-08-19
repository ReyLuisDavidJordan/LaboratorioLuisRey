from typing import Union


def suma(a: int, b: int) -> int:
    return a + b

def division(a: int, b: int) -> Union[float, str]:
    if b == 0:
        return "Error"
    return a / b
