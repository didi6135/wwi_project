from sqlalchemy import Column, Integer, Date, Numeric
from sqlalchemy.orm import relationship
from app.db.modeles import Base

class Mission(Base):
    __tablename__ = 'missions'

    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date, nullable=True)
    airborne_aircraft = Column(Numeric(10, 2), nullable=True)
    attacking_aircraft = Column(Numeric(10, 2), nullable=True)
    bombing_aircraft = Column(Numeric(10, 2), nullable=True)
    aircraft_returned = Column(Numeric(10, 2), nullable=True)
    aircraft_failed = Column(Numeric(10, 2), nullable=True)
    aircraft_damaged = Column(Numeric(10, 2), nullable=True)
    aircraft_lost = Column(Numeric(10, 2), nullable=True)

    targets = relationship("Target", back_populates="mission")

