import mysql.connector as sql
from config import host, user, password, database

db = sql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

print(f'Connected to database: {db.is_connected()}')

cur = db.cursor()

cur.execute("SHOW TABLES;")

for x in cur:
    print(x)
