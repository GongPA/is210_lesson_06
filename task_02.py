#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Task_02.py
  Average of a list
"""

import data
import task_01


def get_average(int_list):
    ''' gets average of list of ints'''

    float_list = [float(i) for i in int_list]

    output = sum(float_list) / len(float_list)

    return output


TOTAL_AVG = get_average(data.TASK_O1)

EVEN_AVG = round(get_average(task_01.evens_and_odds(data.TASK_O1)), 2)

ODD_AVG = round(get_average(task_01.evens_and_odds(data.TASK_O1, False)), 2)

TOT_REPO = '{0:,.2f}'.format(TOTAL_AVG)

EVEN_REPO = '{0:,.2f}'.format(EVEN_AVG)

ODD_REPO = '{0:,.2f}'.format(ODD_AVG)

REPORT = ('Report for: Task 02'
          '\n{0}'
          '\n\tTotal AVG:      {1:>10}'
          '\n\tEven AVG:       {2:>10}'
          '\n\tOdd AVG: {3:>10}').format('-' * 30, TOT_REPO,
                                         EVEN_REPO, ODD_REPO)
print REPORT
