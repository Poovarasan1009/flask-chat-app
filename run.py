#!/usr/bin/env python3
"""
Flask Chat App - Main entry point
Run with: python run.py
"""

from app import app, socketio, db
from config import config
import os

# Get configuration from environment
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# Create tables if they don't exist
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

if __name__ == '__main__':
    # Get host and port from environment or use defaults
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting Flask Chat App on {host}:{port}")
    print(f"Debug mode: {debug}")
    print(f"Configuration: {config_name}")
    
    # Run the app with SocketIO
    socketio.run(
        app,
        host=host,
        port=port,
        debug=debug,
        use_reloader=debug,
        log_output=True,
        allow_unsafe_werkzeug=True
    )