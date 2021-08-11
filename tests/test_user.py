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
            
            
    def test_fetch_one_user(self):
        try:
            self.connection
            obj_one = User()
            wrapper = obj_one.fetch_one_user(10)
            self.assertEqual(len(wrapper),6)
        except (Exception, Error) as error:
             print('Error while connecting to PostgreSQL:', error)
                         

    def test_create_user_record(self):
            try:
                self.connection
                obj_create = User()
                wrapper = obj_create.create_user_record('Lionel', 'Messi', "Paris St Germany")
                self.assertEqual(wrapper,'confirm_return')
            except (Exception, Error) as error:
                print('Error while connecting to PostgreSQL:', error)  
                
                
    def test_update_user_record(self):
            try:
                self.connection
                obj_update = User()
                result = obj_update.update_user_record(13, username = 'amara')
                self.assertEqual(result, 1)     
            except (Exception, Error) as error:
                print('Error while connecting to PostreSQL:', error)
             
        
            
def tearDown(self):
    if self.connection:
        self.cursor.close()                                       
        self.connection.close()        