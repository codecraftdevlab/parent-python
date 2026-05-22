"""
Entry point for the application.

This file contains the main function that starts the API server.
"""

from .api import app
from .config import API_HOST, API_PORT

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=API_HOST, port=API_PORT)