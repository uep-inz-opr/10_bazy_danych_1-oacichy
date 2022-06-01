import csv
import sqlite3

sqlite_con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = sqlite_con.cursor()

cur.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                  to_subscriber data_type INTEGER, 
                  datetime data_type timestamp, 
                  duration data_type INTEGER , 
                  celltower data_type INTEGER);''')

with open('polaczenia_duze.csv','r') as fin: 
    # csv.DictReader uses first line in file for column headings by default
    reader = csv.reader(fin, delimiter = ";") # comma is default delimiter
    next(reader, None)  # skip the headers
    rows = [x for x in reader]
    cur.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);", rows)
    sqlite_con.commit()

class ReportGenerator:
  def __init__(self,connection):
    self.connection = connection
    self.report_text = None

  def generate_report(self):
    cursor = self.connection.cursor()
    sql_query = f"Select sum(duration) from polaczenia"
    cursor.execute(sql_query)
    result = cursor.fetchone()[0]
    self.report_text = result

  def get_report(self):	
    return self.report_text

if __name__ == '__main__':
    rg = ReportGenerator(sqlite_con)
    rg.generate_report()
    print(rg.get_report())
