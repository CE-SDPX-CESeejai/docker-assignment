from flask import Flask, request, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "mysql_container"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "database": os.getenv("DB_NAME", "test_db"),
    "port": int(os.getenv("DB_PORT", 3306))
}


def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USERS")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

@app.route("/users/<int:uid>", methods=["GET"])
def get_user(uid):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USERS WHERE uid = %s", (uid,))
    user = cursor.fetchone()
    conn.close()
    return jsonify(user if user else {"message": "User not found"})

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO USERS (name, age) VALUES (%s, %s)", (data['name'], data['age']))
    conn.commit()
    conn.close()
    return jsonify({"message": "User added successfully"})

@app.route("/users/<int:uid>", methods=["PUT"])
def update_user(uid):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE USERS SET name = %s, age = %s WHERE uid = %s", (data['name'], data['age'], uid))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated successfully"})

@app.route("/users/<int:uid>", methods=["DELETE"])
def delete_user(uid):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USERS WHERE uid = %s", (uid,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
