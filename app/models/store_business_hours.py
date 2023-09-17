from database.base_model import BaseModel
from playhouse.postgres_ext import BigAutoField, BigIntegerField,TextField, DateTimeTZField, TimeField,CharField, ArrayField, IntegerField, BinaryJSONField, TSVectorField

class StoreBusinessHour(BaseModel):
    store_id = BigIntegerField(primary_key = True, null=False)
    dayOfWeek = IntegerField()  # 0=Monday, 6=Sunday
    start_time_local = TimeField()  # in local time
    end_time_local = TimeField()  # in local time