from database.base_model import BaseModel
from playhouse.postgres_ext import TextField,DateTimeField, DateTimeTZField,CharField,BigIntegerField, IntegerField, BinaryJSONField, TSVectorField

class StorePollStatus(BaseModel):
    store_id = BigIntegerField(primary_key = True, null=False)
    timestamp_utc = DateTimeField() #in UTC
    status = CharField()  # 'active' or 'inactive'

    