#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on thur octo 23 15:52:00 2024

@Author: Elijah tinayo
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a school

    Args:
        mongo_collection (Collection): pymongo collection
        **kwargs (dict): school data

    Returns:
        str: id of the inserted school
    """
    return mongo_collection.insert(kwargs)
