import csv
from database.db_session import db
from app.models.store_report import StoreUptimeDowntime
from peewee import BigIntegerField, FloatField


# Establish a database connection
db.connect()

# Report will be generated by querying data from this schema
report_data = StoreUptimeDowntime.select()

#  output CSV file path
output_csv_file = "app/report/report.csv"  

# Writing report data to the CSV file
with open(output_csv_file, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write the CSV header row
    header = ["store_id", "uptime_last_hour", "uptime_last_day", "uptime_last_week",
              "downtime_last_hour", "downtime_last_day", "downtime_last_week"]
    csv_writer.writerow(header)
    
    # Write the data rows
    for record in report_data:
        csv_writer.writerow([record.store_id, record.uptime_last_hour, record.uptime_last_day,
                             record.uptime_last_week, record.downtime_last_hour,
                             record.downtime_last_day, record.downtime_last_week])

# Close the database connection
db.close()
