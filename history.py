import csv
import os
import sqlite3

from datetime import datetime, timedelta


with sqlite3.connect(r'C:\Users\jaisw\AppData\Local\Google\Chrome\User Data\Default\History') as conn:
    conn.text_factory = str
    c = conn.cursor()
    output_file_path = 'chrome_history.csv'
    with open(output_file_path, 'wb') as output_file:
        csv_writer = csv.writer(output_file, quoting=csv.QUOTE_ALL)
        headers = ['URL', 'Title', 'Visit Count', 'Date (GMT)']
        csv_writer.writerow(headers)
        epoch = datetime(1601, 1, 1)
        for row in (c.execute('select url, title, visit_count, last_visit_time from urls')):
            row = list(row)
            url_time = epoch + timedelta(microseconds=row[3])
            row[3] = url_time
            csv_writer.writerow(row)
os.startfile(output_file_path)