from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from newspaper import Article
from gnews import GNews as gn
import json 

"""---------------------------------------------------------------------------------------------------------"""
# # Set up Selenium options
# chrome_options = Options()

# # chrome_options.add_argument("--headless")  # Comment out the headless mode to see the browser
# service = Service('/home/xhulio/Downloads/chromedriver-linux64/chromedriver')  # Path to ChromeDriver

# # Initialize WebDriver for Chrome
# driver = webdriver.Chrome(service=service, options=chrome_options)


"""---------------------------------------------------------------------------------------------------------"""
# Initialize Google News API 
gn = gn(
    language='en',
    country='US',
    period='7d',
    start_date=None,
    end_date=None,
    max_results=10,
    ) 

# Get News by Topic 
topic = 'World' 
news_by_topic = gn.get_news_by_topic(topic)

with open('news_by_topic.json', 'w') as file: 
    json.dump(news_by_topic, file, indent=1)

# # Find topic in Google News 

# # Load the URL
# driver.get('https://www.reuters.com/world/middle-east/palestinians-say-100000-residents-trapped-israels-north-gaza-assault-2024-10-28/')

# # Wait a few seconds to allow the page to fully load
# driver.implicitly_wait(10)  # 10 seconds

# # Get the entire page content
# page_content = driver.page_source

# with open('page_content.html', 'w') as file: 
#     file.write(page_content)
# # Use newspaper3k to parse the article text
# article = Article('')
# article.set_html(page_content)
# article.parse()

# print(article.text)
# driver.quit()


# driver.quit()