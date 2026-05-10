from flask import Flask,request,jsonify,session
from flask_bcrypt import Bcrypt 
from flask_cors import CORS 
from database import engine,Session,Base
from models import User,movie
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
bcrypt = Bcrypt(app)
CORS(app, 
     supports_credentials=True, 
     origins=["https://super-duper-sniffle-695qrvxrg96qhrwrw-5500.app.github.dev"],
     allow_headers=["Content-Type"],
     methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])
Base.metadata.create_all(engine)

@app.route("/register",methods = ["POST"])
def register():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    password = data["password"]
    
    with Session() as db :
        existing_user = db.query(User).filter_by(email=email).first()
        if existing_user:
            return jsonify({"error" : "email already registered !"}), 400
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(name = name,email = email,password = hashed_password)
        db.add(new_user)
        db.commit()
    return jsonify({"message" : "registered successfuly "}) , 201

@app.route("/login",methods = ["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    with Session() as db :
        user = db.query(User).filter_by(email=email).first()

        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error" : "invalid email or password"}), 401
        session["user_id"] = user.id 
        session["user_name"] = user.name
    return jsonify({"message" : f"welcome {user.name} !"}), 200
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message" : "Logged out !"}), 200
@app.route("/movies",methods=["GET"])
def get_movies():
    if "user_id" not in session :
        return jsonify({"error" : "Login first !"}), 401
    with Session() as db :
        movies = db.query(movie).filter_by(user_id =session["user_id"]).all()
        result = [
            {
                "id" : m.id,
                "title" : m.title,
                "genre" : m.genre,
                "watched" : m.watched
            }
            for m in movies
        ]
    return jsonify(result), 200

@app.route("/movies",methods = ["POST"])
def add_movie():
    if "user_id" not in session :
        return jsonify({"error" : "Login first !"}), 401
    data = request.get_json()
    with Session() as db :
        movies = movie(
            title = data["title"],
            genre = data["genre"],
            user_id = session["user_id"]
        )
        db.add(movies)
        db.commit()
    return jsonify({"message" : "Movie added !"}), 201

@app.route("/movies/<int:movie_id>", methods = ["PATCH"])
def mark_watched(movie_id):
    if "user_id" not in session:
        return jsonify({"error" : "Login first !"}), 401
    with Session() as db :
        movies = db.query(movie).filter_by(id = movie_id,user_id = session["user_id"]).first()
        if not movies :
            return jsonify({"error" : "Login first !"}), 404
        movies.watched = True
        db.commit()
    return jsonify({"message" : "marked as watched !"}), 200
@app.route("/movies/<int:movie_id>", methods = ["DELETE"])
def delete_movie(movie_id):
    if "user_id" not in session :
        return jsonify({"error" : "Login first !"}), 401
    with Session() as db :
        movies = db.query(movie).filter_by(id = movie_id,user_id = session["user_id"]).first()
        if not movies :
            return jsonify({"error" : "movie not found !"}), 404
        db.delete(movies)
        db.commit()
    return jsonify({"message" : "movie deleted !"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)