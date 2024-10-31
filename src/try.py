import google_news_api as gna 
import json 

my_api = gna.GoNews() 

news = my_api.get_related_news_by_topic()

with open('news.json', 'w') as file: 
    json.dump(news, file, indent=1)