from database.base_model import BaseModel
from playhouse.postgres_ext import TextField,DateTimeField, DateTimeTZField,CharField,BigIntegerField, IntegerField, BinaryJSONField, TSVectorField
from peewee import BigIntegerField, FloatField

class StoreUptimeDowntime(BaseModel):
    store_id = BigIntegerField(primary_key=True, null=False)
    uptime_last_hour = FloatField()  # Uptime in minutes for the last hour
    uptime_last_day = FloatField()   # Uptime in hours for the last day
    uptime_last_week = FloatField()  # Uptime in hours for the last week
    downtime_last_hour = FloatField()  # Downtime in minutes for the last hour
    downtime_last_day = FloatField()   # Downtime in hours for the last day
    downtime_last_week = FloatField()  # Downtime in hours for the last week
