#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    task_03.py
    Bubble Sort
"""

import data


def bubble_sort(input_list):
    '''bubble sort function'''

    done = None
    while not done:
        done = False
        for i in range(0, len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                done = True
                temp = input_list[i]
                input_list[i + 1] = input_list[i]
                input_list[i] = temp
                return input_list
            # i was using without temp. That working too.
            # this time i use temp to swip those values

print bubble_sort(data.TASK_O1)
