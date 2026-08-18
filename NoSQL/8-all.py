#!/usr/bin/env python3
"""Lists all the documents of a collection."""


def list_all(mongo_collection):
    """Returns the list of all the documents of a collection.

    Args:
        mongo_collection: the pymongo collection object to read.

    Returns:
        A list of documents, empty if the collection has none.
    """
    return list(mongo_collection.find())
