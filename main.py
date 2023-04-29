import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="",
  user="admin",
  password="1qaz2wsx",
  database="test_db"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS customers")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

start_time = datetime.datetime.now()
for i in range(2000):
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (f"John {i}", f"Highway 21-{i}")
    mycursor.execute(sql, val)

mydb.commit()

end_time = datetime.datetime.now()

print(f"Time taken to insert 2 records: {end_time - start_time}")