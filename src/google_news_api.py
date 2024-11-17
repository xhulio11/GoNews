from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from newspaper import Article
from bs4 import BeautifulSoup
from constants import * 
import feedparser
import json
import time
import traceback

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
        feed = feedparser.parse(url)

        # Get the entries: All the news with their related news by other sources 
        entries = feed.entries
        
        """
        list: news_by_topic
        
        This list will contain in every positin a dictionary of related news 
        [
        {"https://news.google.com/...":{"source":source, "title":title},"https://news.google.com/...":{"source":source, "title":title}, ...}, 
        {"https://news.google.com/...":{"source":source, "title":title},"https://news.google.com/...":{"source":source, "title":title}, ...}, 
        ...]
        
        """
        news_by_topic = [{} for _ in entries]

        for i, entry in enumerate(entries): 

            # Parse the html content to extract the other related news 
            # Get the key:summary which is html content
            summary = entry['summary']
            
            # Create a BeautifulSoup instant to parse 
            content = BeautifulSoup(summary, 'html.parser')
            
            # Find all list content 
            list_items = content.find_all('li')

            if list_items:  # If <li> elements exist
                # Loop through each <li> and extract the href, title, and source
                for li in list_items:
                    # Extract the href
                    link = li.find('a')['href'] if li.find('a') else None
                    
                    # Extract the title
                    title = li.find('a').text.strip() if li.find('a') else None
                    
                    # Extract the source
                    source = li.find('font').text.strip() if li.find('font') else None

                    if link:  # Ensure the link is valid before adding to the dictionary
                        news_by_topic[i][link] = {"source": source, "title": title}
            else:  # If no <li> elements, check for a single <a> tag
                single_a = content.find('a')
                
                if single_a:
                    # Extract the href
                    link = single_a['href']
                    
                    # Extract the title
                    title = single_a.text.strip()
                    
                    # Since there's no <li>, we may not have a source font tag
                    source = content.find('font').text.strip() if content.find('font') else None
                    
                    news_by_topic[i][link] = {"source": source, "title": title}

        return news_by_topic
    

    def hard_check_article(self, article): 
            
            print("1.Checking Articles Validity")

            # Title check
            if not article.title or len(article.title.strip()) < 5:
                print("2.Missing or invalid title")
                return False

            # Length check
            if len(article.text) < 100:
                print("2.Content too short")
                return False

            # Keyword filtering (check for terms like "terms of use", "cookies", etc.)
            disallowed_keywords = [
                "terms of use", "privacy policy", "cookies", 
                "about us", "contact us", "login", "sign up"
            ]
            if any(keyword.lower() in article.text.lower() for keyword in disallowed_keywords):
                print("2. Disallowed content keywords found")
                return False

            # Boilerplate or repetitive content check
            if len(set(article.text.split())) / len(article.text.split()) < 0.5:
                print("2. High repetition or boilerplate content detected")
                return False
            
            # Paragraph structure
            paragraphs = article.text.split("\n")
            if len([p for p in paragraphs if len(p.split()) > 10]) < 2:
                print("2.Insufficient paragraph structure")
                return False

            # Media-only check
            if article.movies and len(article.text) < 100:
                print("2.Media-only content")
                return False

            # If all checks pass
            print("2.Valid article")
            return True
    

    def read_articles(self, topics, driver, write_json=False, hard_check_article=False, max_topics = 10):

        articles_by_topic = []

        with open('articles.json', 'w', encoding='UTF-8') as file: 
            
            for counter, topic in enumerate(topics):
                
                articles_content = []

                for url in topic:

                    # Get content using browser 
                    driver.get(url) 

                    try:
                        # Wait for the page to fully load 
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))  # Wait for the body tag

                        # Add a delay to mimic human behavior
                        time.sleep(2) 

                        # Get the page source
                        page_content = driver.page_source

                        # Use newspaper3k to parse the article text
                        article = Article('')
                        article.set_html(page_content)
                        article.parse()

                        # Check articles validity 
                        if hard_check_article and not self.hard_check_article(article): 
                            continue 

                    except TimeoutException:
                        print("An error occurred while loading the page: Page load timed out.")
                        # continue to the other url 
                        continue 

                    except Exception as e:
                        print(f"An error occurred while loading the page: {e}")
                        traceback.print_exc()
                        json.dump(articles_by_topic, file, ensure_ascii=False, )
                        return 

                    # Get the content of the article 
                    article_title = article.title
                    article_text = article.text

                    # Retrieve the source from the topic dictionary
                    article_source = topics[counter][url]["source"]

                    # Append the parsed article content
                    articles_content.append({
                        "content": article_title + '\n' + article_text,
                        "source": article_source
                    })
                    
                    # Mimic human behavior 
                    time.sleep(10)
                                
                articles_by_topic.append(articles_content)

                # This counter is used to keep track of max number of news retrieved 
                counter += 1 

                if counter == max_topics:
                    if write_json: 
                        # Store the content in a file 
                        json.dump(articles_by_topic, file, ensure_ascii=False, indent=1)           

                    driver.quit()
                    break 
        
        return articles_by_topic