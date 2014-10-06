#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    I recommand this code online checker
    ************************
    *http://pep8online.com/*
    ************************
    that help me do use less request from Jenkins server
    ---------------------
    task_04.py
    Cracking passwords
    ---------------------
    This sounds difficult but just call some functions.
    line string connected by ':'
    therefor we have to split it into a list by ':'

    this task will help me understand
    the different between list and tuple.
    Tuples are immutable, and usually contain an heterogeneous sequence of
    elements that are accessed via unpacking (see later in this section)
    or indexing (or even by attribute in the case of namedtuples).
    Lists are mutable, and their elements are usually homogeneous and are
    accessed by iterating over the list.

"""

import data

SALT = "monosodium-glutamate"  #left 2 blanks line before your function name


def crack_it(in_str):
    """ -*- """
    for pw in data.WORDS:
     if data.crypt(pw, SALT) == in_str:
         return pw

     
def test_passwords(pwd):  #don't forget close line by ':'
    """ """
    pw_cracked = []

    for line in pwd:
        fields = line.split(":")
        password = crack_it(fields[1])

        if password:
            pw_cracked.append((password, fields[4]))
    return pw_cracked


def report(out_tuple):
    """ """
    print '\nCracked Passwords\n'
    print '-' * 40

    for i in out_tuple:
        print '{0:<20}{1:<20}'.format(i[0], i[1])


report(test_passwords(data.PASSWD))
