from sqlalchemy import Integer,String,Boolean,Column
from database import Base
class movie(Base):
    __tablename__ = "movies"
    id = Column(Integer,primary_key = True,autoincrement = True)
    title = Column(String(150),nullable = False)
    genre = Column(String(50))
    watched = Column(Boolean,default = False)

    def __repr__(self):
        status = "Watched" if self.watched else "pending"
        return f"{self.id}. {self.title} | {self.genre} | {status}"