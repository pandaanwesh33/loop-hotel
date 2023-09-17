import csv
from peewee import BigIntegerField, CharField, PostgresqlDatabase, Model
from database.db_session import db
from app.models.store_timezone import StoreTimezone

# Establish a database connection
db.connect()

# Read data from the CSV file and insert it into the database
csv_file = "app/csv/timezone.csv"

with open(csv_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        store_id, timezone_str = row
        if not timezone_str:  # Check if timezone_str is empty or null
            timezone_str = "America/Chicago"
        StoreTimezone.create(store_id=store_id, timezone_str=timezone_str)

# Close the database connection
db.close()
