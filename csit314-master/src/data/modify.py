import uuid

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, func
from sqlalchemy.sql import select

def db_connect(filepath):
    db = create_engine(f"sqlite:///{filepath}")
    conn = db.connect()
    meta = MetaData(db)

    if not db.dialect.has_table(conn, "TestCase"):
        Table("TestCase", meta,
                Column("uuid", String, primary_key=True),
                Column("input", String),
                Column("output", String),
                Column("state", Integer)
            ).create(db)
    table = Table("TestCase", meta, autoload=True, autoload_with=db)
    conn.execution_options(autocommit=True)
    return conn, table


def db_disconnect(conn):
    conn.close()


def add_record(data, db, table):
    if data["uuid"] is None:
        data["uuid"] = uuid.uuid4().hex
    statement = table.insert().values(data)
    db.execute(statement)
    return data["uuid"]


def delete_record_by_uuid(uuid, db, table):
    statement = table.delete().where(table.c.uuid == uuid)
    result = db.execute(statement)
    if result.rowcount > 0:
        return True
    return False


def find_record(uuid, db, table):
    query = select([table]).where(table.c.uuid == uuid)
    result = db.execute(query)
    if result.fetchone():
        return True
    return False


def update_record(data, db, table):
    statement = table.update().where(table.c.uuid == data["uuid"]).values(data)
    db.execute(statement)
    return True

def find_count(db, table):
    # Returns a tuple of counts - all records, all records with state = 0, and all records with state = 1
    query1 = select([func.count(table.c.state)]).select_from(table)
    query2 = select([func.count(table.c.state)]).select_from(table).where(table.c.state == 0)
    query3 = select([func.count(table.c.state)]).select_from(table).where(table.c.state == 1)

    result1 = db.execute(query1).scalar()
    result2 = db.execute(query2).scalar()
    result3 = db.execute(query3).scalar()

    results = (result1, result2, result3)
    return results

# meta = MetaData()
# meta.reflect(bind=init_database.engine)
# table = meta.tables.get("TestCase")

