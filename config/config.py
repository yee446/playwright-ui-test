import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://www.google.com")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))
    REPORTS_DIR = os.getenv("REPORTS_DIR", "reports")