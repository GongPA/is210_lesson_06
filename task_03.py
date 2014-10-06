#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    task_03.py
    Bubble Sort
"""


def bubble_sort(input_list):
    '''bubble sort function'''
    
    done = False
    while not done:
        done = True
        for i in range(0, len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                done = False
                temp = input_list[i]
                input_list[i + 1] = input_list[i]
                input_list[i] = temp
        """
        here also can using a temp for swipe list position
        """
    return input_list
