from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from config import Config
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class SentimentService:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        logger.debug("SentimentService initialized with VADER analyzer")

    def analyze_sentiment(self, text: str):
        """
        Analyze the sentiment of the given text using VADER
        Returns a dictionary with 'score' and 'label' properties
        """
        logger.debug(f"Analyzing sentiment for text: {text}")
        
        sentiment_scores = self.analyzer.polarity_scores(text)
        logger.debug(f"Raw VADER scores: {sentiment_scores}")
        
        compound_score = sentiment_scores['compound']
        logger.debug(f"Compound score: {compound_score}")
        
        # Determine sentiment label based on compound score
        if compound_score >= 0.05:
            label = 'positive'
        elif compound_score <= -0.05:
            label = 'negative'
        else:
            label = 'neutral'
            
        result = {
            'score': compound_score,
            'label': label
        }
        logger.debug(f"Final result: {result}")
        return result

    def validate_input(self, data: dict) -> tuple[bool, str]:
        """
        Validate the input data
        Returns: (is_valid, error_message)
        """
        logger.debug(f"Validating input data: {data}")
        
        if not isinstance(data, dict):
            logger.error("Input is not a dictionary")
            return False, "Input must be a JSON object"
        
        if 'data' not in data:
            logger.error("Missing 'data' field")
            return False, "Missing 'data' field in request"
            
        if 'text' not in data['data']:
            logger.error("Missing 'text' field")
            return False, "Missing 'text' field in data"
            
        if not isinstance(data['data']['text'], str):
            logger.error("Text is not a string")
            return False, "Text must be a string"
            
        logger.debug("Input validation successful")
        return True, "" 