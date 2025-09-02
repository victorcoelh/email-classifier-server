from contextlib import asynccontextmanager
import os
from typing import Callable

from fastapi import FastAPI, Request, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import nltk

from src.services.classification import email_classification_service
from src.file_reader import get_text_from_file
from src.models import ClassificationRequest, ClassificationResponse

API_SECRET = os.getenv("API_SECRET")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

@asynccontextmanager
async def lifespan(app: FastAPI):
    nltk.download("wordnet")
    nltk.download("omw-1.4")
    nltk.download("stopwords")
    nltk.download("punkt")
    nltk.download('punkt_tab')
    
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def check_api_secret(request: Request, call_next: Callable) -> Response:
    if request.method == "OPTIONS":
        return await call_next(request)

    if request.headers.get("x-api-key") != API_SECRET:
        return Response(status_code=403, content="Invalid API Key.")

    return await call_next(request)


@app.post("/email/classify-files")
async def classify_email_file(emails: list[UploadFile]) -> list[ClassificationResponse]:
    response = []    
    for email in emails:
        email_content = await get_text_from_file(email)
        response.append(
            (await classify_email(ClassificationRequest(email=email_content)))[0]
        )

    return response

@app.post("/email/classify")
async def classify_email(request: ClassificationRequest) -> list[ClassificationResponse]:
    classification, confidence, answer = email_classification_service(request.email)

    return [ClassificationResponse(
        classification=classification,
        confidence=confidence,
        suggested_answer=answer
    )]
