#!/usr/bin/env python3
"task 6 module"
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "basic annotation"
    return float(sum(mxd_lst))
