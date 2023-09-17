from database.base_model import BaseModel
from playhouse.postgres_ext import DateTimeTZField,CharField


class StoreTimezone(BaseModel):
    store_id = CharField()
    timezone_str = CharField()  # Timezone string, e.g., "America/Chicago"