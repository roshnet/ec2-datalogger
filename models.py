from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase("sensor.db")


class BaseModel(pw.Model):
    class Meta:
        database = db


class Reading(BaseModel):
    sensor_id = pw.CharField(20)
    sensor_type = pw.CharField(20)
    value = pw.FloatField()
    time = pw.DateField(default=datetime.now)

    class Meta:
        db_table = "readings"
