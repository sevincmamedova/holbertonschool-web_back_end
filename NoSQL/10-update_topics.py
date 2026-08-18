#!/usr/bin/env python3
"""Changes all the topics of a school document."""


def update_topics(mongo_collection, name, topics):
    """Replaces the topics of every school matching a given name.

    Args:
        mongo_collection: the pymongo collection object to update.
        name: the name of the school to update.
        topics: the list of topics approached in the school.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
