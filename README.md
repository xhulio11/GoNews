# GoNews 
This is a simple Google News Api. It's main goals is to receive related articles given a provided topic. 

## Table of Contents
- [GoNews Installation](#gonews-installation)
- [Browser Installation](#browser-installation)
- [Find Necessary Paths](#find-necessary-paths)
- [Full Example](#full-example)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## GoNews Installation 
Instructions on how to install and set up your project. For example:
```bash
git clone https://github.com/xhulio11/GoNews.git
cd GoNews
python install -r requirements.txt
```
## Browser Installation
Instructions on how to install and set up the browswer driver. 
Currently only chrome-driver is supported 

- Install Google Chrome if it is not already installed and create a simple profile 
- Donwnload according to your system the [chrome driver](https://googlechromelabs.github.io/chrome-for-testing/)
- Store it in a specific directory, open the driver and create a a simple profile

## Find Necessary Paths 
In examples folder, 3 python scripts are provided to help you set up the projet easily 
- Windows User
  - Find path of the driver i.e: ```C:\\Users\\user\\OneDrive\\Desktop\\Thesis\\chromedriver-win64\\chromedriver.exe```
  - Find path of the profile i.e ```C:\Users\user\AppData\Local\Google\Chrome\User Data```
    - The above path can be found easily running in chrome ```chrome://version/``` and look at <b> Profile Path </b>
  - Set up the paths correctly in ```examples/windows_run.py``` as shown
    ```python
       chrome_options.add_argument(r"--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")
       chrome_options.add_argument(r"--profile-directory=Profile 1") 
    ```
- Linux User
  - Find path of the driver i.e: ```/home/user/Downloads/chromedriver-linux64/chromedriver```
  - Find path of the profile i.e ```/home/user/.config/google-chrome/```
    - The above path can be found easily running in chrome ```chrome://version/``` and look at <b> Profile Path </b>
  - Set up the paths correctly in ```examples/windows_run.py``` as shown
    ```python
       chrome_options.add_argument(r"--user-data-dir=/home/user/Downloads/chromedriver-linux64/chromedriver")
       chrome_options.add_argument(r"--profile-directory=Profile 1") 
    ```
  ## Full Example
  This example shows the usage of api and the outputs of the implemented functinos
  
  ```python
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service
  from selenium.webdriver.chrome.options import Options
  import sys
  import os
  
  # Add the absolute path of the src directory to sys.path
  sys.path.append(os.path.abspath("/home/xhulio/Desktop/Thesis/GNews/src"))
  from google_news_api import *
  
  # Set up Selenium options
  chrome_options = Options()
  
  service = Service('/home/xhulio/Downloads/chromedriver-linux64/chromedriver')  # Path to ChromeDriver
  chrome_options.add_argument(r"--user-data-dir=/home/xhulio/.config/google-chrome/")  # Root directory for Chrome user data
  chrome_options.add_argument(r"--profile-directory=Profile 1")  # The profile folder you created
  
  # Initialize WebDriver for Chrome 
  driver = webdriver.Chrome(service=service, options=chrome_options)
  google_api = GoNews(language='english', country='United States')

  url_news = google_api.get_news_by_topic(topic='POLITICS')
  content = google_api.read_articles(url_news, driver, write_json=True, max_topics=1)
  ```


  ```url_news``` is a list of dictionaries. Every dictionary contains different sources of the same news 
  ```json
   [{
  "https://news.google.com/rss/articles/CBMiowFBVV95cUxPdzZfMkhzZEZ4aC1NNllnN3BDRkxwT1Bodzgwb29ldHBtYXFoU2lOVWM0Y01PZEdNM21XeHVFRUJUUHZDMU0zSEIyOXpzekQxT0hiVTFRZjdpdXlQdVpHMGVIenJsM01MSHRMcEZNN09UZzdLZUk3dk9rLTlZQU92dy01b0JQcmJzZnVDc2VJR3U2WU8wZWlvbHNwTE1UYXN5bFFB0gGYAUFVX3lxTE1CeE5NekFIY1YtNVhHTkY5TjdpS0diVmlOcGhBblI1TEpiWDhUSHA1enJHZW5VdGlLc0xNc1Nnck1EZlB6WlAyQXd6LWtIUjF5QW1uaDNJMm9VM0lHeVVELUUxSXo3R0FFSHpUTkNuN19pY1MzcEFhamY3bUczYnh5bjZQUlhLMmE2amRPUXROc21jeTFEWjZJ?oc=5": "Pawan Sets Up Wing To 'Protect Sanatana Dharma'..",
  "https://news.google.com/rss/articles/CBMi7wFBVV95cUxPQnFXRlJrRS1rMHRDSGdZbVdyaUtzQzRzaDhQaFB2bFVsZFVVM3BjdG1GaVRVVENQUk1Zb2FaYzRpNVNJZlZrLVNRY2JBQmJjeWlVaVZZdGtYbHNrV0RwMXFpZXpZWUtRR0pxaGlDaGJiN1VGMzA3bGhBbnU0T1l5b09uYVQ5ampoZWVXa0NpenVSRDdwMEx4Z3Z1d2NPZmJQaHlNdmdRd19QSUFTTk9saUJPWUZqeGRvckw5ZWx4bDExakNhV3FuLUd0Wmc4bk5mci1nNXh5LXdSeUhud096NENmMHVXNHlnRXE2TEwwMA?oc=5": "Pawan Kalyan starts Sanatana Dharma protection wing in Janasena party: ‘Respect all religion but…’",
  },, ... 
  ```

  
  ```content``` is a list of lists. Every list contais the content of the visited urls above
  ```json
  [['content 1', 'content 2', ...], ['content 3', 'content 4', ...], ...]
  ```
  
