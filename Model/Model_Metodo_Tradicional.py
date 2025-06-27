from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Ejecucion(Base):
    __tablename__ = 'ejecuciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_ejecucion = Column(DateTime, default=datetime.datetime.utcnow)
    data_set = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Ejecucion(id={self.id}, fecha_ejecucion={self.fecha_ejecucion}, data_set={self.data_set})>"
