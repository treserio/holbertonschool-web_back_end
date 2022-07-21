#!/usr/bin/env python3
''' provide stats about Nginx logs stored in MongoDB '''


from pymongo import MongoClient


def loggedStats():
    ''' provide stats about Nginx logs stored in MongoDB '''
    col = MongoClient().logs.nginx

    print(f'{col.count_documents({})} logs')
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print('\n'.join(f'\tmethod {m}: {col.count_documents({"method": m})}'
                    for m in methods))

    print(f'{col.count_documents({"method": "GET", "path": "/status"})} \
        status check')


if __name__ == "__main__":
    loggedStats()
