from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    USER = os.getenv("TARGET_USER")
    PASS = os.getenv("TARGET_PASS")
    HEADLESS = os.getenv("HEADLESS", "True").lower() in ("1","true","yes")
    DATABASE = os.getenv("DATABASE", "results.db")
