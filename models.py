import peeweedbevolve
from peewee import (
    TextField, Model, AutoField, ForeignKeyField
)
from playhouse.shortcuts import model_to_dict
from playhouse.postgres_ext import PostgresqlExtDatabase

from settings.config import PG_CONN

db = PostgresqlExtDatabase(**PG_CONN, server_side_cursors=True)


class BaseModel(Model):

    def as_dict(self, **kwargs):
        return model_to_dict(self, **kwargs)

    class Meta:
        database = db


class Types(BaseModel):
    type = TextField()


class Items(BaseModel):
    id = AutoField(index=True, primary_key=True)
    url = TextField(index=True, unique=True)
    type = ForeignKeyField(
        Types,
        backref='items',
        null=True
    )


if __name__ == '__main__':
    peeweedbevolve.evolve(
        db,
        interactive=False,
        ignore_tables=['basemodel']
    )
