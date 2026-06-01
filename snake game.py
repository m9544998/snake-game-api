from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
DB_NAME = "snake.db"
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        player     TEXT    NOT NULL,
        score      INTEGER NOT NULL,
        level      INTEGER NOT NULL,
        date       TEXT    DEFAULT (date('now'))
    )
    """)
    conn.commit()
    conn.close()
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def home():
    return jsonify({"message": "Snake Game API Running!"})
@app.route('/scores', methods=['GET'])
def get_scores():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC")
    rows = cursor.fetchall()
    conn.close()

    scores = []
    for row in rows:
        scores.append({
            "id":     row["id"],
            "player": row["player"],
            "score":  row["score"],
            "level":  row["level"],
            "date":   row["date"]
        })
    return jsonify({"total": len(scores), "leaderboard": scores})
@app.route('/top', methods=['GET'])
def get_top():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 5")
    rows = cursor.fetchall()
    conn.close()

    top = []
    for i, row in enumerate(rows):
        top.append({
            "rank":   i + 1,
            "player": row["player"],
            "score":  row["score"],
            "level":  row["level"],
            "date":   row["date"]
        })
    return jsonify({"top_5": top})
@app.route('/add_score', methods=['POST'])
def add_score():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scores (player, score, level) VALUES (?, ?, ?)",
        (data["player"], data["score"], data["level"])
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Score saved successfully!"}), 201

@app.route('/player/<string:name>', methods=['GET'])
def get_player(name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM scores WHERE player = ? ORDER BY score DESC",
        (name,)
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return jsonify({"error": "Player not found"}), 404

    scores = [dict(r) for r in rows]
    best   = scores[0]["score"]
    return jsonify({"player": name, "best_score": best, "all_scores": scores})


@app.route('/delete_score/<int:sid>', methods=['DELETE'])
def delete_score(sid):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores WHERE id = ?", (sid,))
    if cursor.fetchone() is None:
        conn.close()
        return jsonify({"error": "Score not found"}), 404

    cursor.execute("DELETE FROM scores WHERE id = ?", (sid,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Score deleted successfully!"})


if __name__ == '__main__':
    init_db()
    print("Snake Game API: http://127.0.0.1:5000")
    app.run(debug=True)