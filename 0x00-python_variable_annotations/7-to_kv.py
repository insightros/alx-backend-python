#!/usr/bin/env python3
"task 7 module"
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "basic annotation"
    return (k, float(v**2))
