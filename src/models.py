from sqlalchemy import Column, Integer, String, Float, Date, Text
from src.database import Base

# This class maps to the PostgreSQL table 'symptom_logs'
class SymptomLog(Base):
    __tablename__ = "symptom_logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    glucose = Column(Float)
    sleep_hours = Column(Float)
    medication = Column(String(255))
    symptoms = Column(Text)
