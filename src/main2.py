from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from newspaper import Article

# Set up Selenium options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode if you don't need a visible browser
service = Service('/usr/local/bin/geckodriver')  # Path to GeckoDriver

# Initialize WebDriver for Firefox
driver = webdriver.Firefox(service=service, options=firefox_options)

# Load the URL and get the final page content
driver.get('https://edition.cnn.com/2024/10/29/politics/kamala-harris-ellipse-speech/index.html')
page_content = driver.page_source

# Use newspaper3k to parse the article text
article = Article('')
article.set_html(page_content)
article.parse()

print(article.text)
driver.quit()
