
from mysql import connector
from config import config

conn = connector.connect(**config)
cursor = conn.cursor()
cursor.execute("SELECT * FROM admin;")
rows = [i for i in cursor]
print(rows)
conn.close()