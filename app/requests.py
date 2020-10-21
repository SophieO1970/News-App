import urllib.request,json
from .models import Article,Source
import os


# Getting api key
api_key = None
# Getting the news base url
base_url = None
source_base_url = None


def configure_request(app):
    global api_key,base_url,source_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    source_base_url = app.config['SOURCES_API_BASE_URL']
    

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(id,api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        print('get_news_url', base_url)
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        image = news_item.get('urlToImage')

        if image:
            news_object = Article(author,title,description,image,url,publishedAt)
            news_results.append(news_object)

    return news_results

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_base_url.format(category,api_key)
    # print(get_news_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)

    return sources_results

def process_sources_results(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        if category:
            source_object = Source(id,name,description,url,category)
            sources_results.append(source_object)

    return sources_results
