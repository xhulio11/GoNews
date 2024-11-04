import google_news_api as gna 
import json 

my_api = gna.GoNews() 

news = my_api.get_related_news_by_topic()

topics = []

for topic in news:
    urls = []
    for url in topic: 
        if type(url) is dict: 
            urls.append(url['url'])
        else:
            urls.append(url)
    topics.append(urls)

with open('urlsss.json', 'w') as file: 
    json.dump(topics, file)

user_data_dir=r"--user-data-dir=C:\Users\xhuli\AppData\Local\Google\Chrome\User Data"
profile=r"--profile-directory=Profile 1"

articles = my_api.read_articles(topics, user_data_dir=user_data_dir, profile=profile,browser_path='C:\\Users\\xhuli\\OneDrive\\Desktop\\Thesis\\chromedriver-win64\\chromedriver.exe')
