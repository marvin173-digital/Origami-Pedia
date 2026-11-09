import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


def query(sql, params=(), fetch=False):
    conn = get_conn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql, params)
            rows = cur.fetchall() if fetch else None
        conn.commit()
        return rows
    finally:
        conn.close()


def init_db():
    query("""
        CREATE TABLE IF NOT EXISTS origami (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            difficulty VARCHAR(10) NOT NULL,
            steps TEXT NOT NULL
        )
    """)
    query("ALTER TABLE origami ADD COLUMN IF NOT EXISTS image VARCHAR(255)")


init_db()


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/origami")
def list_origami():
    difficulty = request.args.get("difficulty")
    if difficulty:
        rows = query(
            "SELECT * FROM origami WHERE difficulty = %s ORDER BY id",
            (difficulty,), fetch=True)
    else:
        rows = query("SELECT * FROM origami ORDER BY id", fetch=True)
    return jsonify(rows), 200


@app.post("/origami")
def add_origami():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    difficulty = data.get("difficulty")
    steps = data.get("steps")
    image = data.get("image")
    if not (name and difficulty and steps):
        return jsonify(error="name, difficulty, steps wajib diisi"), 400
    rows = query(
        "INSERT INTO origami (name, difficulty, steps, image) "
        "VALUES (%s, %s, %s, %s) RETURNING id",
        (name, difficulty, steps, image), fetch=True)
    return jsonify(id=rows[0]["id"], name=name), 201


@app.get("/")
def index():
    difficulty = request.args.get("difficulty")
    if difficulty:
        rows = query(
            "SELECT * FROM origami WHERE difficulty = %s ORDER BY id",
            (difficulty,), fetch=True)
    else:
        rows = query("SELECT * FROM origami ORDER BY id", fetch=True)
    return render_template("index.html", items=rows, active=difficulty)