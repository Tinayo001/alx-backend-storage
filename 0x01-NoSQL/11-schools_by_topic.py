#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July  17 14:54:00 2023

@Author: Tinayo Keiya
"""


def schools_by_topic(mongo_collection, topic: str):
    """
    Returns a list of schools that have a certain topic.

    Args:
        mongo_collection (Collection): A pymongo collection.
        topic (str): The topic to search for.

    Returns:
        List[str]: A list of schools that have a certain topic.
    """
    return list(mongo_collection.find({"topics": topic}))
