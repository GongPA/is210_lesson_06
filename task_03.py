#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  task_03.py
  Bubble Sort
my_list = [13,5,86,17,8,9,10]
done = False
while not done:
  done = True
  for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
      '
        compare the elements in list form index 0 - the end of list
        example: [13,5,86,17,8,9,10]
        5<86
        but 13>5
        therefor it sets the trigger 'done' to active.
        which is false to kick in the while loop.
      '
      done = False
      my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


print my_list
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
