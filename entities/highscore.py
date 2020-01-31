from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class Highscore(Base):
    __tablename__ = 'tb_highscore'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    laptime = Column(String)
    date = Column(TIMESTAMP)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'laptime': self.laptime,
            'date': self.date.strftime('%H:%M:%S %d.%m.%Y'),
        }