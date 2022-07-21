#!/usr/bin/env python3
''' mongoDB module, list all documents of collection '''


def list_all(mongo_collection):
    ''' list all documents in the collection '''
    return mongo_collection.find() if mongo_collection else\
        []
