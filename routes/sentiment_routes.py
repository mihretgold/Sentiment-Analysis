from flask import Blueprint, jsonify, request, send_from_directory
from services.sentiment_service import SentimentService
import asyncio
import os
import logging

logger = logging.getLogger(__name__)

sentiment_bp = Blueprint('sentiment', __name__)
sentiment_service = SentimentService()

@sentiment_bp.route('/')
def index():
    return send_from_directory('static', 'index.html')

@sentiment_bp.route('/api/v1/hello')
def api_hello():
    return jsonify({'message': 'Hello, API!'})

@sentiment_bp.route('/api/v1/data', methods=['POST'])
async def api_data():
    data = request.get_json()
    logger.debug(f"Received request data: {data}")
    
    # Validate input
    is_valid, error_message = sentiment_service.validate_input(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    # Run the model in a thread pool to avoid blocking
    loop = asyncio.get_running_loop()
    sentiment_result = await loop.run_in_executor(None, sentiment_service.analyze_sentiment, data['data']['text'])
    
    # Structure the response as a single object
    response = {
        'sentiment': {
            'score': sentiment_result['score'],
            'label': sentiment_result['label']
        }
    }
    
    logger.debug(f"Sending response: {response}")
    return jsonify(response) 