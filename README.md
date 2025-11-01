# SymTrack API

SymTrack API is a health-tracking REST API that allows users to log daily data for chronic conditions such as diabetes, migraines, or asthma. It uses FastAPI and PostgreSQL to store and analyze symptom trends, generate health alerts, and provide insights for better self-management.

---

## Features
- Log daily data (symptoms, glucose, sleep hours, medications)
- Fetch all logs and recent trends
- Compute average glucose over a custom time period
- Trigger alerts when glucose or sleep patterns are abnormal
- Fully documented endpoints via Swagger UI (`/docs`)

---

## Tech Stack
**Backend:** FastAPI, SQLAlchemy  
**Database:** PostgreSQL  
**Environment:** Python 3.12+, dotenv  
**Visualization (planned):** React + Chart.js Dashboard

---

## Setup & Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/symtrack-api.git
   cd symtrack-api
    ```
   
2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
    ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
    ```
5. **Set up PostgreSQL**
   ```bash
   psql postgres
   CREATE USER symtrack_user WITH PASSWORD 'symtrack123';
   CREATE DATABASE symtrackdb OWNER symtrack_user;
    ```
6. **Create .env**
   ```bash
   DATABASE_URL=postgresql://symtrack_user:symtrack123@localhost:5432/symtrackdb
   ```

8. **Run the app**
   ```bash
   uvicorn src.main:app --reload
   ```
**Visit:** http://127.0.0.1:8000/doc

**Primary URL** https://symtrack-api.onrender.com

---

## Future Plans

- Add analytics endpoints for symptom correlation

- Build a React dashboard for data visualization

- Deploy to Render / Railway / AWS
