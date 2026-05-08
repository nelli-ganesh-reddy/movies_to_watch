# movies_to_watch# 🎬 Movie Watchlist

A simple command-line app to manage your movie watchlist — built with Python, SQLAlchemy, and a cloud MySQL database on Railway.

---

## 📌 Features

- Add movies with title and genre
- View all movies with their watch status
- Mark movies as watched
- Delete movies from the list

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| SQLAlchemy | ORM — interact with DB using Python |
| PyMySQL | MySQL driver — sends queries to DB |
| python-dotenv | Loads secret credentials from `.env` |
| Railway | Cloud MySQL database hosting |

---

## 📁 Project Structure

```
movie-watchlist/
│
├── .env              # DB credentials (never push this to GitHub!)
├── .gitignore        # Ignores .env and pycache
├── database.py       # DB connection and session setup
├── models.py         # Movie table definition
├── main.py           # CRUD operations and CLI menu
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/movie-watchlist.git
cd movie-watchlist
```

### 2. Install dependencies
```bash
pip install sqlalchemy pymysql python-dotenv cryptography
```

### 3. Set up Railway DB
- Go to [railway.app](https://railway.app) and create a free account
- Create a new project → Add MySQL
- Go to your MySQL service → **Connect tab**
- Copy the **public** connection credentials

### 4. Create your `.env` file
```bash
MYSQLHOST=your_public_railway_host
MYSQLPORT=your_public_port
MYSQLDATABASE=railway
MYSQLUSER=root
MYSQLPASSWORD=your_railway_password
```

> ⚠️ Use the **public host and port** from Railway — not the internal ones. The internal host only works when your app is deployed on Railway itself.

### 5. Run the app
```bash
python main.py
```

> 💡 Make sure to run this in the **terminal**, not the output panel — the app needs interactive input.

---

## 🚀 Usage

```
🎬 Movie Watchlist
1. Add Movie
2. View All Movies
3. Mark as Watched
4. Delete Movie
5. Exit
```

---

## 🔐 Important

- Never push your `.env` file to GitHub
- Make sure `.gitignore` includes `.env`
- Your data lives on Railway's servers — safe even if you close the app

---

## 📚 Learnings

This project covers:
- Connecting Python to a cloud MySQL database
- Using SQLAlchemy ORM for database operations
- Managing secrets securely with environment variables
- Basic CRUD operations with a relational database
