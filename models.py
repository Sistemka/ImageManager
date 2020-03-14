import peeweedbevolve
from peewee import (
    TextField, Model, AutoField, ForeignKeyField
)
from playhouse.shortcuts import model_to_dict
from playhouse.postgres_ext import PostgresqlExtDatabase

from settings.config import MONGO_CONN, MONGO_DB

from pymongo import MongoClient

client = MongoClient(**MONGO_CONN)
mngdb = getattr(client, MONGO_DB)
Items = mngdb.items

