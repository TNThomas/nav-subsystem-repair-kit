from statistics import median
from typing import Iterator, List, Tuple

from validator import validate


def score_corrupt_char(char: str) -> int:
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137

def score_corrupt_line(validated: Tuple[bool, str]) -> int:
    valid, details = validated
    if valid or (details[0] in "([{<"):
        result = 0    
    else:
        result = score_corrupt_char(details[0])
    print(result)
    return result
    
def score_corrupt_lines(lines: Iterator[str]) -> int:
    total_score = 0
    for line in lines:
        validated = validate(line)
        total_score += score_corrupt_line(validated)
    return total_score


def score_incomplete_chars(chars: str) -> int:
    result = 0
    for char in chars[::-1]:
        result *= 5
        if char == '(':
            result += 1
        elif char == '[':
            result += 2
        elif char == '{':
            result += 3
        elif char == '<':
            result += 4
    return result

def score_incomplete_line(validated: Tuple[bool, str]) -> int:
    valid, details = validated
    if valid or (details[0] in ")]}>"):
        result = 0    
    else:
        result = score_incomplete_chars(details)
    print(result)
    return result
    
def score_incomplete_lines(lines: Iterator[str]) -> int:
    scores: List[int] = []
    for line in lines:
        line_score = score_incomplete_line(validate(line))
        if line_score > 0:
            scores.append(line_score)
    return median(scores)
