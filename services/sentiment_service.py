from transformers import pipeline
from config import Config
import asyncio

class SentimentService:
    def __init__(self):
        self.model = pipeline("sentiment-analysis", model=Config.MODEL_NAME)

    def analyze_sentiment(self, text: str):
        """
        Analyze the sentiment of the given text
        """
        return self.model(text)

    def validate_input(self, data: dict) -> tuple[bool, str]:
        """
        Validate the input data
        Returns: (is_valid, error_message)
        """
        if not isinstance(data, dict):
            return False, "Input must be a JSON object"
        
        if 'data' not in data:
            return False, "Missing 'data' field in request"
            
        if 'text' not in data['data']:
            return False, "Missing 'text' field in data"
            
        if not isinstance(data['data']['text'], str):
            return False, "Text must be a string"
            
        return True, "" 