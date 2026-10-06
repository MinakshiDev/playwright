import time
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

WEBSITE_URL = os.getenv("PROJECT_URL", "https://example.com/")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(WEBSITE_URL)
    time.sleep(5)  
    browser.close()




    
    


