class Sources:
    """ Sources class to define the news source objects """

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
 

 
class Articles:
    """ Articles class to define the articles object """

    def __init__(self, author, title, description, urlToImage, url, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt   
        
        
    def save_article(self):
        article.all_articles.append(self)


    @classmethod
    def clear_articles(cls):
        article.all_articles.clear()

    @classmethod
    def get_articles(cls,title):

        response = []

        for article in cls.all_articles:
            if article.title == title:
                response.append(article)

        return response        