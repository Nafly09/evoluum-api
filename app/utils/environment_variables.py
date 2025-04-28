import os
from dotenv import load_dotenv


load_dotenv()

STATIC_AUTH_TOKEN = os.getenv('STATIC_AUTH_TOKEN', 'super_secret_token')

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/postgres')