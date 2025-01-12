import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    print("API key found!")
else:
    print("API key not found!")
