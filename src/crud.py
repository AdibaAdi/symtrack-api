from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import func
from datetime import timedelta, date

# Create a new log entry
def create_log(db: Session, log: schemas.SymptomLogCreate):
    db_log = models.SymptomLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# Fetch multiple log entries
def get_logs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.SymptomLog).offset(skip).limit(limit).all()

# Average glucose for recent N days
def get_average_glucose(db: Session, days: int = 7):
    start_date = date.today() - timedelta(days=days)
    avg_glucose = db.query(func.avg(models.SymptomLog.glucose)).filter(models.SymptomLog.date >= start_date).scalar()
    return round(avg_glucose, 2) if avg_glucose else None

# Simple alert check
def get_alerts(db: Session):
    alerts = []
    high_glucose = db.query(models.SymptomLog).filter(models.SymptomLog.glucose > 180).all()
    low_sleep = db.query(models.SymptomLog).filter(models.SymptomLog.sleep_hours < 5).all()

    if high_glucose:
        alerts.append({"type": "High Glucose", "count": len(high_glucose)})
    if low_sleep:
        alerts.append({"type": "Low Sleep", "count": len(low_sleep)})

    return alerts
