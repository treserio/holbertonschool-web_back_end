#!/usr/bin/env python3
''' mongoDB module: finding specific docs '''


def schools_by_topic(mongo_collection, topic):
    ''' returns schools with given topic '''
    return mongo_collection.find({'topics': topic})
