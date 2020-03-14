from pymongo import MongoClient
from settings.config import MONGO_CONN, MONGO_DB


client = MongoClient(**MONGO_CONN)
mngdb = getattr(client, MONGO_DB)
Items = mngdb.items
