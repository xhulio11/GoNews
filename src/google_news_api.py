from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import feedparser
from newspaper import Article
from bs4 import BeautifulSoup
import json,time
from constants import * 


class GoNews():
    
    def __init__(self, language="english", country="United States"):

        # Check validity of language 
        if language not in AVAILABLE_LANGUAGES: 
            raise Exception(f'The language: {language} you provided does not exist.')
        else: 
            self.language = AVAILABLE_LANGUAGES[language] 

        # Check validity of country 
        if country not in AVAILABLE_COUNTRIES: 
            raise Exception(f'The country: {country} you provided does not exist.')
        else: 
            self.country = AVAILABLE_COUNTRIES[country]

        # example of query: "hl=en-US&gl=US&ceid=US%3Aen" 
        self.query = "hl=" + self.language + "-" + self.country + "&gl=" + self.country + "&ceid=" +self.country + "%3A" + self.language
    

    def create_url(self, code=None, query_parameter=None):
        
        # Set the proper url based on the selection of Main topics (WORLD, BUISNESS, ...) or sections (POLITICS, SPORTS ..)
        try: 
            # Check the topic to be used
            if code in TOPICS: 
                url = GOOGLE_NEWS_URL + '/news/rss/headlines/section/topics/' + code + '?' + query_parameter
                return url 
            
            elif code in SECTIONS.keys():
                url = GOOGLE_NEWS_URL + '/rss/topics/' + SECTIONS[code] + '?' +  query_parameter
                return url      
        except:
            print("ERROR: Some variable is not defined properly for the creation of the url")


    def get_news_by_topic(self, topic="POLITICS"):
        # Get News by main provided topics in google news site 
        url = self.create_url(code=topic, query_parameter=self.query)
        # Take the XML content 
        feed = feedparser.parse(url,)

        # Get the entries: All the news with their related news by other sources 
        entries = feed.entries
        
        """
        list: news_by_topic
        
        This list will contain in every positin a dictionary of reated news 
        [
        {"title 1": "https://news.google.com/...", "title 2": "https://news.google.com/..."}, 
        {"title 3": "https://news.google.com/...", "title 4": "https://news.google.com/..."}, 
        ...]
        
        """
        news_by_topic = [None for _ in entries]

        for i, entry in enumerate(entries): 

            # Get main title and the url 
            title = entry['title']
            
            url = entry["links"][0]['href']
            
            # Add the first article in the current position
            news_by_topic[i] = {url:title}

            # Parse the html content to extract the other related news 
            # Get the key:summary which is html content
            summary = entry['summary']
            
            # Create a BeautifulSoup instant to parse 
            content = BeautifulSoup(summary, 'html.parser')
            
            # Every li tag contains href: link, target: title 
            a_tags = content.find_all('a')
            j = 0 
            for a_tag in a_tags:

                # Get url and title of current article 
                url = a_tag.get('href')
                title = a_tag.get_text(strip=True)  # Extracts the text content

                # Add it in the dictionary 
                news_by_topic[i][url] = title 

        return news_by_topic


    def read_articles(self, topics, browser_path, user_data_dir, profile):
        # Set up Selenium options
        chrome_options = Options()
        # Use the custom user profile (make sure to use the correct profile path)
        chrome_options.add_argument(user_data_dir)  # Root directory for Chrome user data
        chrome_options.add_argument(profile)  # The profile folder you created

        service = Service(browser_path)  # Path to ChromeDriver

        # Initialize WebDriver for Chrome
        driver = webdriver.Chrome(service=service, options=chrome_options)
        articles_by_topic = []
        i = 0
        with open('artilces.json', 'w') as file: 
            for topic in topics:
                articles_content = []

                for url in topic:
                    print(i)
                    i += 1
                    driver.get(url)      
                    try:
                        # Wait for the page to fully load (customize as needed)
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))  # Wait for the body tag

                        # Optional: Add a delay to mimic human behavior
                        time.sleep(2)  # Sleep for 2 seconds

                        # Get the page source
                        page_content = driver.page_source

                        # Use newspaper3k to parse the article text
                        article = Article('')
                        article.set_html(page_content)
                        article.parse()

                    except Exception as e:
                        print(f"An error occurred: {e}")
                    time.sleep(10)
                    artilce_title = article.title
                    article_text = article.text
                    articles_content.append(artilce_title + '\n' + article_text)

                articles_by_topic.append(articles_content)
                if i == 20: break

            json.dump(articles_by_topic, file)
            
        # quit Browser
        driver.quit()

        return articles_by_topic
    
        