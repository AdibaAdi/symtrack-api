from pydantic import BaseModel
from datetime import date

# Shared attributes
class SymptomLogBase(BaseModel):
    date: date
    glucose: float
    sleep_hours: float
    medication: str
    symptoms: str

# Used for POST requests (creating a new log)
class SymptomLogCreate(SymptomLogBase):
    pass

# Used for GET responses (includes ID)
class SymptomLogResponse(SymptomLogBase):
    id: int

    class Config:
        # Converts ORM objects into response models
        from_attributes = True
