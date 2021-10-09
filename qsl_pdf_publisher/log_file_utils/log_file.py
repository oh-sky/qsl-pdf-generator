"""
LogFile class module
"""
from typing import NamedTuple


class LogFile(NamedTuple):
    """
    named tuple which has basename and path
    """
    basename: str
    path: str
