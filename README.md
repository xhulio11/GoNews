# GoNews 
This is a simple Google News Api. It's main goal is to receive related articles given a provided topic. 

## Table of Contents
- [GoNews Installation](#gonews-installation)
- [Browser Installation](#browser-installation)
- [Find Necessary Paths](#find-necessary-paths)
- [Full Example](#full-example)
  - [get_news_by_topic](#get_news_by_topic)
  - [read_articles](#read_articles)

## GoNews Installation 
Instructions on how to install and set up your project. For example:
```bash
git clone https://github.com/xhulio11/GoNews.git
cd GoNews
python install -r requirements.txt
```
## Browser Installation
Instructions on how to install and set up the browser driver. 
Currently only chrome-driver is supported 

- Install Google Chrome if it is not already installed and create a simple profile 
- Donwnload according to your system the [chrome driver](https://googlechromelabs.github.io/chrome-for-testing/)
- Store it in a specific directory, open the driver

**NOTE**
* It is strongly recommended to install [I still don't care about cookies](https://chromewebstore.google.com/detail/i-still-dont-care-about-c/edibdbjcniadpccecjdfdjjppcpchdlm) extension
  to avoid cookie pop ups. 

## Find Necessary Paths 
In <b>examples</b> folder, 2 python scripts are provided to help you set up the projet easily 
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
  
  service = Service('/home/user/Downloads/chromedriver-linux64/chromedriver')  # Path to ChromeDriver
  chrome_options.add_argument(r"--user-data-dir=/home/user/.config/google-chrome/")  # Root directory for Chrome user data
  chrome_options.add_argument(r"--profile-directory=Profile 1")  # The profile folder you created
  
  # Initialize WebDriver for Chrome 
  driver = webdriver.Chrome(service=service, options=chrome_options)
  google_api = GoNews(language='english', country='United States')

  ```
  ### get_news_by_topic
  ```python
  # a list of dictionaries. Every dictionary contains different sources of the same news
  url_news = google_api.get_news_by_topic(topic='POLITICS')
  ```
  ```json
   [{
  "https://news.google.com/rss/articles/CBMingFBVV95cUxQMFJiY24zcVcwWkFGbnRtckFtSFpITkxzVWZHeWpHVlp4azhtUDhvTjFRUjM5eUl5QXQ2dTN5U2tIb2s1T1RjSWdwY1dlSDh5Y2d1VkE3NHd1SFFkdEktNU9vZ2V1UTZKWXVpeWZPRGRySm5ENVZ3TFFvUXZjVXV4aENqSmFUZkRPQ25Pdjhnb3FHRWFiSDc2NmJwTHNwQQ?oc=5": {
   "source": "Fortune",
   "title": "Cathie Wood says Elon Musk will succeed in his audit of the federal government because he has 'more proprietary data' than anyone"
  },
  "https://news.google.com/rss/articles/CBMiVkFVX3lxTE9CTGlWVkhNUkFEWE4zYkNIdzR1cW1RSGJFS1ZYWHh1R3I5YXlfeU1vb3FhdFU5SkJkRWJGcFJmSV9uMWkzemNfcnhVaE40SjNLU1l4WHdn?oc=5": {
   "source": "Fox News",
   "title": "Dem senator reveals his amusement over appointment of Musk, Ramaswamy for DOGE"
  },
  "https://news.google.com/rss/articles/CBMirgFBVV95cUxNMW1WXzg4cG9peXpFVnlnVTUyU1pGdWhYYlNqbWQ5QmQxejgzQXlRdkR1UVoxbXRabDZBWEtjX19DT2hMeUNEZVlxSGpuSy01Njdub1pKdXpycEN1SV9fRDVtWjJncE91d01acVR3bmE2QkpNdXZVV19fUEkzQUh6amVqN0ZGTVNnakJlTUNnS3N5SlRnY09XVHlpc0l6cHd6TjhkdlhLcDNPQ2JMaXc?oc=5": {
   "source": "The New York Times",
   "title": "What Can the Department of Government Efficiency Do?"
  },
  "https://news.google.com/rss/articles/CBMiuAFBVV95cUxOeUhQWWJZNF9wN015OHJ1czB1S2t6cVVKcXVVbHhvN2FyY0h6SldLWkpNck5URFZpSUlwSEh1eXAyenoxQUVodTBGYk5Nc2YwV1VxZkR4Q3J0WjQ3Wl9rRWlsWEp0UkhWSlFXN2llQnVxclJENzJBdV94WnJDR0V6M0VmQ0xyYlAxWUU3bGIwZXZPS09NemtCa09kVHJ4bjVsaUI4eHNYbVJObGNCenpXRTNOQkdOOHhM?oc=5": {
   "source": "USA TODAY",
   "title": "Before Elon Musk, Trump tapped another billionaire to cut costs. It didn't end well"
  },
  {
    "...": "More data here as a placeholder"
  }
  ```
  ### read_articles
  ``` python
  # a list of lists. Every list contais the content of the visited urls above
  # url_news must have been extracted first 
  content = google_api.read_articles(url_news, driver, write_json=True, max_topics=1)
  ```
  ```json
    [
      [{"content 1", "source 1"},{"content 1", "source 2"},{"content 3", "source 3"}],
      [{"content 4", "source 4"},{"content 5", "source 5"},{"content 6", "source 6"}]
      ["// more arrays go here"]
    ]
  ```
