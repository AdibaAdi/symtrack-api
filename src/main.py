from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src import models, schemas, crud
from src.database import engine, SessionLocal

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request


# Create tables automatically if missing
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for DB session handling
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root message
@app.get("/")
def root():
    return {"message": "Welcome to SymTrack API. Visit /docs to explore endpoints"}

# Add a new symptom log
@app.post("/log/", response_model=schemas.SymptomLogResponse)
def create_log(log: schemas.SymptomLogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db=db, log=log)

# Fetch all logs
@app.get("/logs/", response_model=list[schemas.SymptomLogResponse])
def read_logs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_logs(db=db, skip=skip, limit=limit)

# Average glucose trend
@app.get("/trends/average_glucose")
def get_average_glucose(days: int = 7, db: Session = Depends(get_db)):
    avg = crud.get_average_glucose(db, days)
    if avg:
        return {"average_glucose": avg, "days": days}
    return {"message": f"No glucose data for the past {days} days."}

# Alert endpoint
@app.get("/alerts/")
def get_alerts(db: Session = Depends(get_db)):
    results = crud.get_alerts(db)
    if not results:
        return {"message": "No alerts — all values within healthy range."}
    return {"alerts": results}


templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    logs = crud.get_logs(db=db)
    return templates.TemplateResponse("dashboard.html", {"request": request, "logs": logs})

