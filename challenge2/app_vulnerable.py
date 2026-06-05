from flask import Flask, request
import os
import sqlite3
import pickle

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host')
    result = os.system(f"ping -c 1 {host}")
    return str(result)

@app.route('/user')
def get_user():
    username = request.args.get('name')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query)

    return str(cursor.fetchall())

@app.route('/load', methods=['POST'])
def load_data():
    data = pickle.loads(request.data)
    return str(data)

if __name__ == "__main__":
    app.run(debug=True)