import unittest
import psycopg2
from psycopg2 import Error
from models.user import *
from unittest import result

class TestUser(unittest.TestCase):
    def setUp(self):
        self.connection = psycopg2.connect(                            # initialize connection to PostgreSQL
        user = 'decagon',
        database = 'postgres')
        self.cursor = self.connection.cursor()                         # initialize a cursor to communicate with database
        self.obj_all = User()
        
    def test_fetch_all_users(self):
        try:
            self.connection
            wrapper = len(self.obj_all.fetch_all_users())
            self.assertIsNot(wrapper, None)  
        except (Exception, Error) as error:
            print('Error while connecting to PostgreSQL:', error)
            
def tearDown(self):
    if self.connection:
        self.cursor.close()                                       
        self.connection.close()        