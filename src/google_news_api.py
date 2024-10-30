from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from newspaper import Article
from gnews import GNews 
import requests
from bs4 import BeautifulSoup
import json 

GOOGLE_URL_TOPICS = 'https://news.google.com/topics/'

class GoNews(Gnews):
    
    def __init__(self, language="en", country="US", max_results=100, period=None, start_date=None, end_date=None,
                 exclude_websites=None, proxy=None):

        # Inherit from the Gnews module 
        super().__init__(self, language="en", country="US", max_results=100, period=None, start_date=None, end_date=None,
                 exclude_websites=None, proxy=None)
        

    def get_related_news_by_topic(self, topic = 'World'):
        
        # Get main articles on the choosen topic  
        news_by_topic = self.get_news_by_topic(topic)

        for article in news_by_topic: 

            # Take the url of the article 
            url = article['url']

            # Find identifier 
            identifier = url.split("/articles/")[1]
