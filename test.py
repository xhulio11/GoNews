from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import SessionNotCreatedException
import time 
import subprocess 
import sys
import os
import json 

# Add the absolute path of the src directory to sys.path
sys.path.append(os.path.abspath("/home/xhulio/Desktop/GoNews/src"))
from google_news_api import *
from mongod_db import * 


def get_chrome_driver():
    # Set up Selenium options
    chrome_options = Options()
    service = Service('/usr/bin/chromedriver') 
    chrome_options.add_argument('--disable-notifications')
    # If you have a specific user-data and profile:
    chrome_options.add_argument("--user-data-dir=/home/xhulio/.config/chromium/")
    chrome_options.add_argument("--profile-directory=Profile 2")

    return webdriver.Chrome(service=service, options=chrome_options)

def kill_chrome_processes():
    # Attempts to kill all Chromium/Chrome processes.
    # If your system uses `chromium-browser`, adjust accordingly.
    subprocess.run(["pkill", "-9", "chromium"], check=False)
    subprocess.run(["pkill", "-9", "chrome"], check=False)

try:
 driver = get_chrome_driver()

except SessionNotCreatedException as e:
 print("SessionNotCreatedException encountered. Attempting to kill Chrome/Chromium and retry...")
 kill_chrome_processes()
 time.sleep(1)  # small delay to ensure processes are fully shut down
 # Attempt to re-initialize
 driver = get_chrome_driver()
except Exception as e:  
 print("Some undefined error occured")
 exit()

# MongoDB connection details
MONGO_HOST = "192.168.2.13"  # Replace with your computer's IP
MONGO_PORT = 27017           # Default MongoDB port
DATABASE_NAME = "balanced_news"     # Name of the database to use
COLLECTION_NAME = "google_articles" # Name of the collection to use

google_api = GoNews(language='english', country='United States')

print("Receiving urls")
url_news = google_api.get_news_by_topic(topic='POLITICS')

print(url_news)
# with open("urls.json", "w", encoding="UTF-8") as file: 
#     json.dump(url_news, file,indent=4)

print("Receiving Content")
content = google_api.read_articles(url_news, driver, write_json=True, max_topics=5)

client = mongodb(MONGO_HOST, MONGO_PORT, DATABASE_NAME, COLLECTION_NAME)

client.insert_articles(content)
