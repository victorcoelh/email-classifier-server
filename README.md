# Email Classifier - Backend Server

An API built with FastAPI for classifying e-mails as productive or unproductive. Integrates with
Google Gemini via OpenAI API for classification.

### Features
- Classifies e-mails as productive or unproductive
- Provides a confidence level for each classification
- Accepts .txt and .pdf files via the endpoint /classify-files/
- Accepts raw text via the endpoint /classify/

### Environment Variables

Before running the server, you'll need to provide three environment variables:
- ```GEMINI_API_KEY``` -> An API key for the Google Gemini LLM (used for classification)
- ```API_SECRET``` -> An authentication key. Requests to this server must include this value in the "x-api-key" header.
- ```FRONTEND_URL``` (Optional) - Frontend URL for CORS validation. Defaults to http://localhost:5173.

### Installation

#### Using Docker

1. Make sure you have (Docker installed)[https://docs.docker.com/engine/install/]

2. Build the API image:
```docker build --tag email-api .```

3. Run the server:
```docker run -p 8080:8080 email-api --env-file ./.env email-api```

#### Whitout Docker (Using UV)

[UV](https://docs.astral.sh/uv/getting-started/installation/) is a Rust-based package manager for Python
that simplifies virtual environments and dependency management, while also providing faster installs
and builds than pip.

1. Install UV

2. Install dependencies in an isolated virtual environment:
```uv sync``` (uv automatically creates a .venv folder)

3. Run the server:
```uv run uvicorn src.server:app --host 0.0.0.0 --port 8080```

## API Endpoints

### POST /classify/
Classifies raw text.

#### Request Body:
```json
{
  "text": "The content of the e-mail goes here."
}
```

#### Response Body:
```json
[
  {
    "classification": "productive",
    "confidence": 0.92,
    "suggested_answer": "Your response suggestion here."
  }
]
```

### POST /classify-files/
Classify e-mails from file uploads (.txt or .pdf).

#### Request Body:
```json
{
  "emails": [ /* array of files */ ]
}
```

#### Response Body:
```json
[
  {
    "classification": "unproductive",
    "confidence": 0.85,
    "suggested_answer": "Your response suggestion here."
  }
]
```
