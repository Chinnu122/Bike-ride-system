# Entry point is handled by run.py calling create_app from __init__.py
# But we can put the main FastAPI/Flask app creation logic here if needed.
# For now, it's in __init__.py. This file was listed in the structure.
from app import create_app

app = create_app()
