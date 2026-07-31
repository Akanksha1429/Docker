from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

@app.route('/')
def home():
    return {
        "message": "Welcome to the Employee App with PostgreSQL!"
    }

@app.route("/employees")
def employees():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees 
    (id SERIAL PRIMARY KEY, name VARCHAR(100), 
    position VARCHAR(100));
    """)

    conn.commit()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    employees = []

    for row in rows:
        employees.append({
            "id": row[0],
            "name": row[1],
            "position": row[2]
        })
    return jsonify(employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
