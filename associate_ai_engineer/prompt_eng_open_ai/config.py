from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file once

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")