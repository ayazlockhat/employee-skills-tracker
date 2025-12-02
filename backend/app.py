from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
import os

from routes.employees_routes import employees_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["employee_db"]
app.db = db

# Register routes
app.register_blueprint(employees_bp, url_prefix="/employees")

@app.route('/Health')
def health_check():
    try:
        app.db.command("ping")
        return {"Status": "OK", "Message": "Server is running"}, 200
    except Exception as e:
        return {"Status": "Error", "Message": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)