"""
Averages for ages and scores.

Start with the simplest working code; then refactor to remove duplication,
and finally consider using built-ins (e.g., sum) for clarity and speed.
All inputs are basic floats, no Union types.
"""

from typing import List

def average_age(ages: List[float]) -> float:
    """
    Compute the arithmetic mean of ages.

    Args:
        ages: Non-empty list of ages as floats.

    Returns:
        The average age as a float.

    Examples:
        >>> average_age([20.0, 22.0, 24.0])
        22.0
    """
    raise NotImplementedError


def average_score(scores: List[float]) -> float:
    """
    Compute the arithmetic mean of scores.

    Args:
        scores: Non-empty list of scores as floats.

    Returns:
        The average score as a float.

    Examples:
        >>> average_score([90.0, 95.0, 85.0])
        90.0
    """
    raise NotImplementedError
