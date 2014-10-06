#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    task_01.py
    Even and Odds()
"""

import data

def evens_and_odds(numbers, show_even=True):
    """
        accepts numbers as list object
        and show_even as bool...
        returns new list of even or odd numbers
    """

listout = []

if show_even:
    for i in numbers:
        if i % 2 == 0:
            listout.append(i)

elif not show_even:
    for i in numbers:
        if i % 2 != 0:
            listout.append(i)

return listout
