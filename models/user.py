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
                
                
    def create_user_record(self,*arg):
            try:
                self.connection
                create_query = ('INSERT INTO users (username, first_name, last_name) VALUES (%s, %s, %s)')      # Formated SQL query
                values = arg
                self.cursor.execute(create_query, values)                                           # executes the SQL query
                self.connection.commit()                                                            # commits the tansaction to database
                confirm_record = self.cursor.rowcount                                         # confirms the number of input to database
                print(f'you have inserted {confirm_record} into users table successfully')
                return confirm_record
            except (Exception, Error) as error:
                print(('Error! Could not connect to Postgres server:', error))
            finally:
                if self.connection:
                    self.cursor.close()                                                
                    self.connection.close()    
                    
                    
    def update_user_record(self, args,**kwargs):
        try:
                self.connection
                column_name, value = list(kwargs.items())[0]
                if column_name == 'username':                
                    update_query = ('UPDATE users SET username = (%s) WHERE user_id = (%s);')            # Updating SQL 
                    self.cursor.execute(update_query, (value, args))                                     # executes the SQL query
                elif column_name == 'first_name':                
                    update_query = ('UPDATE users SET first_name = (%s) WHERE user_id = (%s);')          # Updating SQL 
                    self.cursor.execute(update_query, (value, args))       
                elif column_name == 'last_name':                
                    update_query = ('UPDATE users SET last_name = (%s) WHERE user_id = (%s);')     
                    self.cursor.execute(update_query, (value, args))      
                
                self.connection.commit()                                  # commits the transaction to databse
                confirm_record = self.cursor.rowcount                     # confirms the number of updated rows
                return confirm_record
        except (Exception, Error) as error:
            print(('Error while connecting to PostgreSQL:', error))
        finally:
            if self.connection:
                self.cursor.close()    
                self.connection.close()                 