from flask import Flask, json, request, jsonify
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.secret_key = "66ca6ce5e12b0f9be579227c99fec184"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_SORT_KEYS'] = False

mysql = MySQL(app)


@app.route('/')

def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    users = []
    content = {}
    for result in data:
        content = {
            'id': result['_id'],
            'email': result['email'],
            'username': result['username'],
            'password': result['password'],
            'firstname': result['first_name'],
            'lastname': result['last_name'],
            'verified': result['verified'],
            'archived': result['archived']
        }
        users.append(content)
        content = {}
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)