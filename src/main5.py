import requests
from bs4 import BeautifulSoup
import json 


URL = "https://news.google.com/rss/articles/CBMixwFBVV95cUxPT3JsbmRYOE5obG43SFpMcHNMdVdJZjJ3bGRfbEw0X29XdUhXRnVyWktRUjR4YXFXRnJZUWZsMHQ0cU9tYWJQc1dBbExLUUc5UWN3ZjFaZkFJaWczZDU4RGhFWjBHd3laQXdqemlFSjh4NGNEZDZMdjY1OEw1OWFkVWpCWEZMQVplT1pWVXdZTGhWa0ZFRnI5ellJTGIwaF9aNzJkRFZHbDZIV0lTeXFtLXNKVXRuUDFISFNyaktzclk3OVBUZW9J?oc=5&hl=en-US&gl=US&ceid=US:en",

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


with open('news_by_topic.json', 'r') as file: 
    content = json.load(file)

url = content[0]['url']
identifier = url.split("/articles/")[1]
print(identifier)
article = soup.find('a', href=lambda x: x and identifier in x)
print(article.prettify())

article = soup.find('article', jsdata=lambda x: x and identifier in x)


# Find the parent <div> of the <a> tag
# sub_articles = article.find_all_next('article')
# sub_article = sub_articles[0]
# jsdata = sub_article.get('jsdata')
# print(jsdata)