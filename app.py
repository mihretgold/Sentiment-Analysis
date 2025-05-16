from flask import Flask
from flask_cors import CORS
from routes.sentiment_routes import sentiment_bp
from config import Config
import os

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(sentiment_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)