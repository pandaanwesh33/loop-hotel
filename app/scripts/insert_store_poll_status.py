import csv
import psycopg2
from database.db_session import db
from datetime import datetime
from app.models.store_poll_status import StorePollStatus


# Establish a database connection
db.connect()

# Read data from the CSV file and insert it into the database
csv_file = "app/csv/store_status.csv"  

with open(csv_file, 'r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row 
    for row in csv_reader:
        store_id, timestamp_utc_str, status = row
        timestamp_utc = datetime.strptime(timestamp_utc_str, "%Y-%m-%d %H:%M:%S")  # Parse the timestamp string
        StorePollStatus.create(store_id=store_id, timestamp_utc=timestamp_utc, status=status)

# Close the database connection
db.close()