from typing import Tuple


def matches(start: str, end: str) -> bool:
    return (
        (start == "(" and end == ")")
        or (start == "[" and end == "]")
        or (start == "{" and end == "}")
        or (start == "<" and end == ">")
    )

def validate(s: str) -> Tuple[bool, str]:
    """
    Returns whether the string is valid, and a details string
    """
    stack: str = ""
    for char in s:
        if char in "([{<":
            stack += char
        elif char in ")]}>":
            if (stack.__len__() > 0) and matches(stack[-1], char):
                stack = stack[:-1]
            else:
                return (False, char)
    return (
        stack == "",
        stack
    )