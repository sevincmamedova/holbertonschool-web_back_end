#!/usr/bin/env python3
"""Finds the schools having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of schools having a given topic.

    Args:
        mongo_collection: the pymongo collection object to search.
        topic: the topic to look for.

    Returns:
        A list of documents, empty if no school approaches that topic.
    """
    return list(mongo_collection.find({"topics": topic}))
