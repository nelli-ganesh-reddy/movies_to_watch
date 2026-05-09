from sqlalchemy import Integer,String,Boolean,Column,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True,autoincrement = True)
    name = Column(String(100),nullable = False)
    email = Column(String(100),nullable = False,unique = True)
    password = Column(String(200),nullable = False)
    movies = relationship("movie",back_populates = "user")
    def __repr__(self):
        return f"{self.id} | {self.name} | {self.email}"
class movie(Base):
    __tablename__ = "movies"
    id = Column(Integer,primary_key = True,autoincrement = True)
    title = Column(String(150),nullable = False)
    genre = Column(String(50))
    watched = Column(Boolean,default = False)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User",back_populates = "movies")
    def __repr__(self):
        status = "Watched" if self.watched else "pending"
        return f"{self.id}. {self.title} | {self.genre} | {status}"