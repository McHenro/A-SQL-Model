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
         
         
    def test_fetch_one_book(self):
        try:
            self.connection
            obj_one = Book()
            wrapper = obj_one.fetch_one_book(10)
            self.assertEqual(len(wrapper),6)                           # To assert that the length of the return value is must be 6
        except (Exception, Error) as error:
            print(('Error while connecting to PostgreSQL:', error))
            
    
    def test_create_book_record(self):
        try:
            self.connection
            obj_create = Book()
            wrapper = obj_create.create_book_record(9, 'Programming languages book 1', "2005")  # assert that nos. of record created is updated
            self.assertEqual(wrapper,1)
        except (Exception, Error) as error:
            print('Error while connecting to PostgreSQL:', error)  

    
    def test_update_book_record(self):
        try:
            self.connection
            obj_update = Book()
            wrapper = obj_update.update_book_record(1009, book_name = 'Decadevs')    # assert that nos. of changes made is updated
            self.assertEqual(wrapper,1)
        except (Exception, Error) as error:
            print('Error while connecting to PostgreSQL:', error) 
            
                
    def test_delete_book_record(self):
            try:
                self.connection
                obj_delete = Book()
                wrapper = obj_delete.delete_book_record(1029)
                if wrapper >= 0:
                    self.assertAlmostEqual(wrapper,0)                           # assert nos. deletion made is greater or equal to one
            except (Exception, Error) as error:
                print('Error while connecting to PostgreSQL:', error)
  
            
    def tearDown(self):
        if self.connection:
            self.cursor.close()                                       
            self.connection.close()    
            

    