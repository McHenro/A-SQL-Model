import psycopg2
from psycopg2 import Error


class User:
    def __init__(self):
        self.connection = psycopg2.connect(                     # Connect to an existing database
            user= 'decagon',
            database = 'mchenro_db')
        self.cursor = self.connection.cursor()                  # Create a cursor to perform database operations
        
    def fetch_all_users(self):                                  # Fetch all users available
        try:
            self.connection
            self.cursor.execute('SELECT * FROM users;')         # Executing a SQL query 
            query_result = self.cursor.fetchall()                     # Fetch result
            return query_result
        except (Exception, Error) as error:
            print(('Error! Could not connect to Postgres server:', error))
        finally:
            self.cursor.close()                                 # terminates cursor operation
            self.connection.close()                             # terminates connection operation
            
            
    def fetch_one_user(self,args):                              # Fetch one user by id
            try:
                self.connection
                self.cursor.execute(f'SELECT * FROM users WHERE user_id = {args};')
                query_result= self.cursor.fetchone() 
                return query_result
            except (Exception, Error) as error:
                print(('Error! Could not connect to Postgres server:', error))
            finally:
                self.cursor.close()
                self.connection.close()