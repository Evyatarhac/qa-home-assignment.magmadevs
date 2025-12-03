import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def generate_token():
    refresh_token = os.getenv("REFRESH_TOKEN")
    url = f"{BASE_URL}/api/auth/generate"

    response = requests.post(url, json={"refresh_token": refresh_token})
    response.raise_for_status()

    data = response.json()
    return data["access_token"]
