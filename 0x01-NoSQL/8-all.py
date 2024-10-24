#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Octo  17 15:02:25 2024

@Author: Elijah Tinayo
"""
from typing import List


def list_all(mongo_collection) -> List[dict]:
    """
    List all documents in a collection

    Args:
        mongo_collection (Collection): collection to list

    Returns:
        List[dict]: list of documents
    """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
