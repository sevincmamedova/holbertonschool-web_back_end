#!/usr/bin/env python3
"""Inserts a document in a collection."""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection, built from the keyword args.

    Args:
        mongo_collection: the pymongo collection object to write to.
        **kwargs: the fields of the new document.

    Returns:
        The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
