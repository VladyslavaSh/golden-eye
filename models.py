from peewee import (SqliteDatabase, Model, IntegerField, DoubleField, DateTimeField, datetime as peewee_datetime, CharField, TextField)

from config import DB_NAME

db = SqliteDatabase(DB_NAME)


class _Model(Model):
    class Meta:
        database = db


class XRate(Model):
    class Meta:
        db_table = "xrates"
        indexes = (
            (("from_currency", "to_currency"), True),
        )

    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    updated = DateTimeField(default=peewee_datetime.datetime.now)

    def __repr__(self):
        return "XRate(%s=>%s): %s" % (self.from_currency, self.to_currency, self.rate)


# logging of request-response info into the DB
class ApiLog(_Model):
    class Meta:
        db_table = "api_logs"

    request_url = CharField()
    request_data = TextField(null=True)
    request_method = CharField(max_length=100)
    request_headers = TextField(null=True)
    response_text = TextField(null=True)
    # with a creation of the table the index will be created
    created = DateTimeField(index=True, default=peewee_datetime.datetime.now)
    finished = DateTimeField()
    error = TextField(null=True)


# logging of error info into the DB
class ErrorLog(_Model):
    class Meta:
        db_table = "error_logs"

    request_data = TextField(null=True)
    request_url = TextField()
    request_method = CharField(max_length=100)
    error = TextField()
    traceback = TextField(null=True)
    created = DateTimeField(default=peewee_datetime.datetime.now, index=True)


def init_db():
    XRate.drop_table()
    XRate.create_table()
    XRate.create(from_currency=840, to_currency=980, rate=1)
    XRate.create(from_currency=978, to_currency=980, rate=1)
    XRate.create(from_currency=1000, to_currency=840, rate=1)

    for m in (ApiLog, ErrorLog):
        m.drop_table()
        m.create_table()


    print("db created!")
