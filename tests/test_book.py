import unittest
import psycopg2
from psycopg2 import Error
from models.book import *

class TestUser(unittest.TestCase):
    def setUp(self):
        self.connection = psycopg2.connect(                            # creating connection to PostgreSQL
        user = 'decagon',
        database = 'postgres')
        self.cursor = self.connection.cursor()                         # creating a cursor to communicate with database
        self.obj_all = Book()
        
    def test_fetch_all_book(self):
        try:
            self.connection
            wrapper = len(self.obj_all.fetch_all_book())
            self.assertIsNot(wrapper, None)                            # To assert that the return value is never a None
        except (Exception, Error) as error:
            print(('Error while connecting to PostgreSQL:', error))
            
    def tearDown(self):
        if self.connection:
            self.cursor.close()                                       
            self.connection.close()    
            

    