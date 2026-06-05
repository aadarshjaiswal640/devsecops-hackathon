from flask import Flask, request
import sqlite3
import json
import subprocess
import re

app = Flask(__name__)

@app.route('/ping')
def ping():

    host = request.args.get('host')

    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host", 400

    result = subprocess.run(
        ["ping", "-n", "1", host],
        capture_output=True,
        text=True
    )

    return result.stdout

@app.route('/user')
def get_user():

    username = request.args.get('name')

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE name = ?",
        (username,)
    )

    return str(cursor.fetchall())

@app.route('/load', methods=['POST'])
def load_data():

    data = json.loads(request.data)

    return str(data)

if __name__ == "__main__":
    app.run(debug=True)