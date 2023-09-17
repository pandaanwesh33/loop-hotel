from database.db_session import db

from models.store_business_hours import StoreBusinessHour
from app.models.store_timezone import StoreTimezone
from models.store_timezone import StoreTimezone


def create_tables():
    try:
        db.create_tables([StoreBusinessHour, StoreTimezone, StoreTimezone])
        db.close()
        print("created table")
    except:
        print("Exception while creating table")
        raise