from dotenv import load_dotenv
import os 
load_dotenv()

class Config:
    FLASK_APP=os.getenv("FLASK_APP")
    FLASK_DEBUG=os.getenv("FLASK_DEBUG")
    FLASK_ENV=os.getenv("FLASK_ENV")
