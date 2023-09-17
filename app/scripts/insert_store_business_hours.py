import csv
import psycopg2
from database.db_session import db

# CSV file path
csv_file_path = "app/csv/store_business_hours.csv"

# Default values
default_values = {
    "start_time_local": "00:00:00",  # Default value for 'start_time_local' column
    "end_time_local": "23:59:59",    # Default value for 'end_time_local' column
}

# Connect to the PostgreSQL database
# conn = psycopg2.connect(**db_params)
db.connect()
cursor = db.cursor()

# Open the CSV file and skip the header
with open(csv_file_path, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Skip the header row
    next(csv_reader, None)
    
    # Process the remaining rows
    for row in csv_reader:
        store_id = int(row.get("store_id"))  
        day_of_week = int(row.get("dayOfWeek"))
        start_time_local = row.get("start_time_local", default_values["start_time_local"])
        end_time_local = row.get("end_time_local", default_values["end_time_local"])

        # Inserting the data into the database using a cursor
        cursor.execute(
            "INSERT INTO storebusinesshour (store_id, dayOfWeek, start_time_local, end_time_local) "
            "VALUES (%s, %s, %s, %s)",
            (store_id, day_of_week, start_time_local, end_time_local)
        )

# Commit the changes and close the database connection
# conn.commit()
# conn.close()
db.commit()
db.close()
