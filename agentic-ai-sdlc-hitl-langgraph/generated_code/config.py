"""
Configuration file for the application.

This file contains environment setup and constants used throughout the application.
"""

import os

# Database connection settings
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = int(os.environ.get('DB_PORT', 3306))
DB_USERNAME = os.environ.get('DB_USERNAME', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'order_database')

# OAuth 2.0 authentication settings
OAUTH_CLIENT_ID = os.environ.get('OAUTH_CLIENT_ID', 'client_id')
OAUTH_CLIENT_SECRET = os.environ.get('OAUTH_CLIENT_SECRET', 'client_secret')

# API settings
API_HOST = os.environ.get('API_HOST', 'localhost')
API_PORT = int(os.environ.get('API_PORT', 8080))