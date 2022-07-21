#!/usr/bin/env python3
''' mongoDB module: for insert '''


def insert_school(mongo_collection, **kwargs):
    ''' insert new doc into collection using kwargs '''
    return mongo_collection.insert_one(kwargs).inserted_id
