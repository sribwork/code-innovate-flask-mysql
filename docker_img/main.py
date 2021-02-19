import os
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def default_page():
   return "hello world"

@app.route('/users', methods=['GET'])
def get_items():
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM test_db.test_table")
   rv = cur.fetchall()
   payload = []
   content = {}
   for result in rv:
      content = {'id': result[0], 'firstname': result[1], 'lastname': result[2]}
      payload.append(content)
      content = {}
   return jsonify(payload) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
