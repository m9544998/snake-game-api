# snake game API

A simple REST API built with **Python Flask** and **SQLite**.

---

## Requirements

```bash
pip install flask
```

---

## Project Structure

```
shop/
├── snakegame_api.py   # Main API file
├── snake game.db       # SQLite database (auto-generate hoga)
└── README.md
```
Installation
1. Clone the project
bashgit clone https://github.com/yourname/snake-game.git
cd snake-game
---

## who to run

```bash
python snake game_api.py
```

Server start:
```
http://127.0.0.1:5000
```
API Endpoints
MethodEndpointDescriptionGET/Game pageGET/leaderboardTop scores pagePOST/save-scoreScore save karo (JSON)GET/api/scoresScores JSON format mein
---
POST /save-score — Request Body
json{
  "player": "Abdullah",
  "score": 250
}
GET /api/scores — Response
json[
  { "player": "Abdullah",   "score": 250, "date": "2026-06-01 10:30:00" },
  { "player": "Sara",  "score": 180, "date": "2026-06-01 09:15:00" }
]


## Tech Stack
Notes

SQLite database file snake_game.db automatically run
Production mein debug=False .
Game logic frontend () mein hai; Flask sirf scores handle karta hai.

# coder:
```
Maheen Asad
```
- **Language:** Python 3
- **Framework:** Flask
- **Database:** SQLite3
- **Format:** JSON
