#!/usr/bin/env python3
''' mongoDB module: update many docs '''


def update_topics(mongo_collection, name, topics):
    ''' updates all the topics of a school(name) '''
    return mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
