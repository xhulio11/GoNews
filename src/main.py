import feedparser
import json 
from bs4 import BeautifulSoup
from google_news_api import *

google_api = GoNews()

a = google_api.get_news_by_topic(topic='POLITICS')

with open('news.json', 'w', encoding='UTF-8') as file: 
    json.dump(a, file, indent=1)