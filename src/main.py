# from gnews import GNews as gn
# import json 
# from newspaper import Article

# google_news = gn()
# top_news = google_news.get_top_news()

# with open('file.json', 'w') as file:
#     json.dump(top_news, file, indent=1)

# #url = 'https://news.google.com/rss/articles/CBMijgFBVV95cUxPWGE1VHJOdVlGd0xYakJDNnd1Z3R1bzFGWGd4bTM5VC1WU19JUVVqYUQ1OXlzcDJaRXFFdmEwOVRsZ3p4YUdhZ1AzdURNb2RxRmFmLWRSQmZfWkFQa1hKNHlxc21jSUdiaVZaT0kxdXNXeVhYaERoTXhqZUF3djZwS0VlRXppXzZPYWgtZ3V30gGEAUFVX3lxTE1tVkdXRUlGX3l4NmxSTmdJQVo2MFV2VWtfMDItWTA4Q3RoYU9zT1ozc1I2SnRpQXZQTktRYjY0MDhHamVGY0hJbDM0T1c5Vkd1TTlrYzNfSXhCVU4xTFNlUHRVcE51Nm9YLS1fYW5lNWNDZ1RIZnB4SmdfUFdnVVk0LVN1Xw?oc=5&hl=en-US&gl=US&ceid=US:en'

# url = 'https://edition.cnn.com/2024/10/29/politics/kamala-harris-ellipse-speech/index.html'

# article = Article(url)

# article.download()
# article.parse()

# print(article.text)

import requests
from newspaper import Article

# Initial Google News RSS URL
url = 'https://news.google.com/rss/articles/CBMijgFBVV95cUxPWGE1VHJOdVlGd0xYakJDNnd1Z3R1bzFGWGd4bTM5VC1WU19JUVVqYUQ1OXlzcDJaRXFFdmEwOVRsZ3p4YUdhZ1AzdURNb2RxRmFmLWRSQmZfWkFQa1hKNHlxc21jSUdiaVZaT0kxdXNXeVhYaERoTXhqZUF3djZwS0VlRXppXzZPYWgtZ3V30gGEAUFVX3lxTE1tVkdXRUlGX3l4NmxSTmdJQVo2MFV2VWtfMDItWTA4Q3RoYU9zT1ozc1I2SnRpQXZQTktRYjY0MDhHamVGY0hJbDM0T1c5Vkd1TTlrYzNfSXhCVU4xTFNlUHRVcE51Nm9YLS1fYW5lNWNDZ1RIZnB4SmdfUFdnVVk0LVN1Xw?oc=5&hl=en-US&gl=US&ceid=US:en'

# Follow the redirection
response = requests.get(url, allow_redirects=True)
final_url = response.url  # This should be the CNN URL or similar

# Use the final URL with newspaper3k
article = Article(final_url)
article.download()
article.parse()

print(article.text)
