from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from newspaper import Article

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode if you don't need a visible browser
service = Service('/home/xhulio/Downloads/chromedriver-linux64/chromedriver')  # Path to ChromeDriver

# Initialize WebDriver for Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the URL and get the final page content
driver.get('https://www.reuters.com/world/middle-east/palestinians-say-100000-residents-trapped-israels-north-gaza-assault-2024-10-28/')
page_content = driver.page_source

# Use newspaper3k to parse the article text
article = Article('')
article.set_html(page_content)
article.parse()

print(article.text)
driver.quit()
