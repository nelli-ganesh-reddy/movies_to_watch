from database import engine,Session,Base
from models import movie
Base.metadata.create_all(engine)
def add_movie():
    title = input("Movie title : ")
    genre = input("Movie genre : ")
    with Session() as session :
        m = movie(title = title, genre = genre)
        session.add(m)
        session.commit()
    print(f"{title} added to watch list !")
def view_movies():
    with Session() as session :
        movies = session.query(movie).all()
        if not movies :
            print("No movies yet !")
        for m in movies:
            print(m)
def mark_watched():
    view_movies()
    movie_id = int(input("Enter the movie id to mark as watched : "))
    with Session() as session :
        m = session.query(movie).filter_by(id = movie_id).first()
        if m :
            m.watched = True
            session.commit()
            print(f"{m.title} marked as watched !")
        else:
            print("movie not found !")
def delete_movie():
    view_movies()
    movie_id = int(input("enter movie id to delete : "))
    with Session() as session :
        m = session.query(movie).filter_by(id=movie_id).first()
        if m :
            session.delete(m)
            session.commit()
            print(f"{m.title} deleted!")
        else:
            print("movie not found !")
def menu():
    while True:
        print("movie watch list")
        print("1. add movie to list")
        print("2. view all movies on list")
        print("3. mark as watched")
        print("4. Delete movie")
        print("5. Exit")
        choice = int(input("enter ur choice : "))
        if(choice == 1):
            add_movie()
        elif(choice == 2):
            view_movies()
        elif(choice == 3):
            mark_watched()
        elif(choice == 4):
            delete_movie()
        elif(choice == 5):
            break
        else :
            print("invalid input")   
menu()