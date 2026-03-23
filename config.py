
"""this is minimal config file to load environment variables and set up the GenAI client"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
PROJECT_ROOT = Path(__file__).parent
load_dotenv(PROJECT_ROOT / ".env")

#API KEY CONFIGURATION
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

#LLM CONFIGURATION
DEFAULT_MODEL = "gemini-2.5-flash"
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

#Processing CONFIGURATION
DEFAULT_BATCH_SIZE = 10
STREAMLIT_BATCH_SIZE = 5