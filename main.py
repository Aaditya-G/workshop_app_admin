from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes import configure_routes
from supabase import create_client, Client
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

configure_routes(app, supabase)

if __name__ == '__main__':
    app.run(debug=True)