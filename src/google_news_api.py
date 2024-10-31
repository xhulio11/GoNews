from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from newspaper import Article
from gnews import GNews 
import requests
from bs4 import BeautifulSoup
import json 


WORLD_URL = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen'
GOOGLE_URL_TOPICS = 'https://news.google.com/topics/'
GOOGLE_URL_READ = 'https://news.google.com/read/'

class GoNews(GNews):
    
    def __init__(self, language="en", country="US", max_results=100, period=None, start_date=None, end_date=None,
                 exclude_websites=None, proxy=None):

        # Inherit from the Gnews module 
        super().__init__(language, country, max_results, period, start_date, end_date,
                 exclude_websites, proxy)
        

    def get_related_news_by_topic(self, url=WORLD_URL, topic = 'World'):
        
        # Take Google News Page 
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        # Get main articles on the choosen topic  
        news_by_topic = self.get_news_by_topic(topic)

        # This list will store all the articles. 
        # Every element will be another list with articles in a json format 
        all_articles = []
        for article in news_by_topic: 
            # Take the url of the article 
            url = article['url']

            # url example: https://news.google.com/rss/articles/, 
            # article_code: {CBMiz ... dzFDb3I1THpxM3RqOWlhQQ} ,
            # article_code_ending = {?oc=5&hl=en-US&gl=US&ceid=US:en}
            # Find identifier 

            first_split = url.split("/articles/")[1]
            article_code = first_split.split("?")[0]
            article_code_ending = '?' + first_split.split("?")[1]

            # find the current main article 
            tag_article = soup.find('article', jsdata=lambda x: x and article_code in x)

            # find the div that contains similar articles 
            div = tag_article.find_next_sibling('div')

            # No other articles are found 
            if div is None: 
                continue

            # Get the articles 
            similar_articles = div.find_all('article')
            
            # Add the main article 
            similar_article_list = [article]    
 
            # Loop through the articles 
            for secondary_article in similar_articles: 
                # Get important info 
                jsdata = secondary_article.get('jsdata')

                # Split it appropriatly
                code = jsdata.split(';')[1]

                # Create url
                created_url =  GOOGLE_URL_READ + code + article_code_ending  
                
                # Add to the list 
                similar_article_list.append(created_url)
            
            all_articles.append(similar_article_list)
        
        return all_articles