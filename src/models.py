from typing import Literal
from pydantic import BaseModel

type EmailType = Literal["Productive", "Unproductive"]


class ClassificationResponse(BaseModel):
    classification: EmailType
    confidence: float
    suggested_answer: str
    
class ClassificationRequest(BaseModel):
    email: str
