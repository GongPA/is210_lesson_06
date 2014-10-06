#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    task_03.py
    Bubble Sort
"""

import data


def bubble_sort(input_list):
    '''bubble sort function'''

    done = False
    while not done:
        done = True
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                done = False
            input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
        """
        here also can using a temp for swipe list position
        """
    return list
