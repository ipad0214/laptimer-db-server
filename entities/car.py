from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class Car(Base):
    __tablename__ = 'tb_cars'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_name = Column(String)
    img = Column(String)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.car_name,
            'img': self.img
        }