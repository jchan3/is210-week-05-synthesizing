#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01."""


import datetime


CURDATE = None


def get_current_date():
    """Gets the current date.

    Args:
        Does not take any parameters.

    Returns:
        date: The current day.

    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
