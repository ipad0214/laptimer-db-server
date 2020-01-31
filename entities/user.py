from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class User(Base):
    __tablename__ = 'tb_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    favorite_car = Column(String)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'favoriteCar': self.favorite_car
        }