#!/usr/bin/env python3
"task 10 module"
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    "basic annotation"
    if lst:
        return lst[0]
    else:
        return None
