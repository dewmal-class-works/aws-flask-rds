from flask import Flask

import mysql.connector

app = Flask(__name__)
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '1qaz2wsx'
app.config['MYSQL_DB'] = 'test_db'

conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (name, address) VALUES (%s, %s)', ('John', 'john@example.com'))
    conn.commit()
    return 'Added user: John'

if __name__ == '__main__':
    mycursor = conn.cursor()
    mycursor.execute("DROP TABLE IF EXISTS customers")
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    app.run(debug=True)
