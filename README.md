# Sentiment Analysis API

A Flask-based REST API for sentiment analysis using the BERT model.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file (optional):
```
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
```

## Running the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET /
- Health check endpoint
- Returns: "Hello, World!"

### GET /api/v1/hello
- Test endpoint
- Returns: `{"message": "Hello, API!"}`

### POST /api/v1/data
- Sentiment analysis endpoint
- Request body:
```json
{
    "data": {
        "text": "Your text here"
    }
}
```
- Returns: Sentiment analysis results

## Project Structure

```
.
├── app.py              # Main application entry point
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── routes/            # API routes
│   └── sentiment_routes.py
└── services/          # Business logic
    └── sentiment_service.py
``` 