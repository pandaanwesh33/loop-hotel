from database.base_model import BaseModel
from playhouse.postgres_ext import DateTimeTZField,CharField,BigIntegerField


class StoreTimezone(BaseModel):
    store_id = BigIntegerField(primary_key = True, null=False)
    timezone_str = CharField()  # Timezone string, e.g., "America/Chicago"