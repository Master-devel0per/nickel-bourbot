from env import db_uri
def get_database():
    from pymongo import MongoClient
    import pymongo
    CONNECTION_STRING = db_uri
    client = MongoClient(CONNECTION_STRING)
    return client['node-stuff']
if __name__ == "__main__":
    dbname = get_database()

dbname = get_database()
collection_name = dbname['banks']

