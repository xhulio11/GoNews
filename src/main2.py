from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from newspaper import Article
import time 

# Set up Selenium options
chrome_options = Options()
service = Service('C:\\Users\\xhuli\\OneDrive\\Desktop\\Thesis\\chromedriver-win64\\chromedriver.exe')  # Path to GeckoDriver
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--remote-debugging-pipe')
#executable_path=r'C:\\Users\\xhuli\\OneDrive\\Desktop\\Thesis\\chromedriver-win64\\chromedriver.exe'
# Use the custom user profile (make sure to use the correct profile path)
chrome_options.add_argument(r"--user-data-dir=C:\Users\xhuli\AppData\Local\Google\Chrome\User Data")  # Root directory for Chrome user data
chrome_options.add_argument(r"--profile-directory=Profile 1")  # The profile folder you created

# Initialize WebDriver for Firefox
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the URL and get the final page content
driver.get("https://news.google.com/rss/articles/CBMiowFBVV95cUxQNkpVVldYU3B4MDdTUE1LMDEzNzdHOVBSdkJ5VTIzX0kwNHMtX1VFdWpiVHZsUmNVUlFvN040QzNkdTd4OXY1Zkl1ZkxJc05YSm5ieDVaOW9aanpsU2ZLU0hFUWtJZ1NLZVplUUxTU2V6MjEybWtUM3lGRmV3cVdtSjZTZU90M2czbWQtdlF4cE9ZdkJEY2V1dS1IWmVwaHkzamVv?oc=5&hl=en-US&gl=US&ceid=US:en")
page_content = driver.page_source

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

    # Print the article text
    print(article.text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()  # Ensure the driver quits even if an error occurs