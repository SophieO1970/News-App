import unittest
from app.models import Articles

class TestArticles(unittest.TestCase):

    def setUp(self):
        self.new_articles = Articles("author",
                                     "title",
                                     "China plans a digital version of its currency, which some say could become a big global payment system.",
                                     "https://image.tmdb.org/t/ptfukyy",
                                     "https://www.bbc.co.uk/news/business-54261382",
                                     "2020-09-24T23:16:08Z")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Articles.all_articles = []

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


    # def test_check_instance_variables(self):
    #     self.assertEquals(self.new_articles.author,'author')
    #     self.assertEquals(self.new_articles.title,'title')
    #     self.assertEquals(self.new_articles.description,'China plans a digital version of its currency, which some say could become a big global payment system.')
    #     self.assertEquals(self.new_articles.urlToImage,"https://image.tmdb.org/t/ptfukyy")
    #     self.assertEquals(self.new_articles.url,'https://www.bbc.co.uk/news/business-54261382')
    #     self.assertEquals(self.new_articles.publishedAt,'2020-09-24T23:16:08Z')


    # def test_save_articles(self):
    #     '''
    #     test_save_article test case to test if the article object is saved into
    #      the article list
    #     '''
    #     self.new_articles.test_save_articles() # saving the new article
    #     self.assertEqual(len(Articles.all_articles),1)
