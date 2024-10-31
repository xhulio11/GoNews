# Take the url of the article 
url = article['url']

# url example: https://news.google.com/rss/articles/, 
# article_code: {CBMiz ... dzFDb3I1THpxM3RqOWlhQQ} ,
# article_code_ending = {?oc=5&hl=en-US&gl=US&ceid=US:en}
# Find identifier 

first_split = url.split("/articles/")[1]
article_code = first_split.split("?")[0]
article_code_ending = first_split.split("?")[1]

# Get the content of the page
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


# find the current main article 
article = soup.find('article', jsdata=lambda x: x and article_code in x)

# find the div that contains similar articles 
div = article.find_next_sibling('div')

# Get the articles 
similar_articles = div.find_all('article')

similar_article_list = [url]    
# Loop through the articles 
for secondary_article in similar_articles: 
    # Get important info 
    secondary_article.get('jsdata')

    # Split it appropriatly
    code = secondary_article.split(';')[1]

    # Create url
    created_url =  GOOGLE_URL_READ + code + article_code_ending  
    
    # Add to the list 
    similar_article_list.append(created_url)

all_articles.append(similar_article_list)