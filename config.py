from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    PORT = int(os.getenv('FLASK_PORT', 5000))
    MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment" 