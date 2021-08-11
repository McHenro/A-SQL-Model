import psycopg2
from psycopg2 import Error


class Book:
    def __init__(self):
        self.connection = psycopg2.connect(                     # Connect to an existing database
            user= 'decagon',
            database = 'mchenro_db')
        self.cursor = self.connection.cursor()                  # Create a cursor to perform database operations
        
    def fetch_all_book(self):
        try:
            self.connection
            self.cursor.execute('SELECT * FROM books;')               # Executing a SQL query 
            query_result = self.cursor.fetchall()                     # Fetch result
            return query_result
        except (Exception, Error) as error:
            print(('Error! Could not connect to Postgres server:', error))
        finally:
            self.cursor.close()                                 # terminate cursor 
            self.connection.close()                             # terminate the connection
       
       
              
    def fetch_one_book(self,args):
        try:
            self.connection
            self.cursor.execute(f'SELECT * FROM books WHERE user_id = {args};')
            query_result= self.cursor.fetchone() 
            return query_result
        except (Exception, Error) as error:
            print(('Error! Could not connect to Postgres server:', error))
        finally:
            self.cursor.close()
            self.connection.close()   
       
       
    def create_book_record(self,*arg):
        try:
            self.connection
            create_query = ('INSERT INTO books (user_id,book_name, pages) VALUES (%s, %s, %s)')      # Inserting formated SQL query
            values = arg
            self.cursor.execute(create_query, values)                                 # executes the SQL query
            self.connection.commit()                                                  # commits the operations to database
            confirm_record = self.cursor.rowcount                                     # confirms the number of input made to database
            return confirm_record
        except (Exception, Error) as error:
            print(('Error! Could not connect to Postgres server:', error))
        finally:
            if self.connection:
                self.cursor.close()                                                 # terminates cursor operation
                self.connection.close()                                             # terminates connection operation
    
            
    def update_book_record(self, args,**kwargs):
            try:
                    self.connection
                    column_name, value = list(kwargs.items())[0]
                    if column_name == 'book_name':                
                        update_query = ('UPDATE books SET book_name = (%s) WHERE book_id = (%s);')     # Updating SQL query
                        self.cursor.execute(update_query, (value, args))                               # executes the SQL query
                    elif column_name == 'pages':                
                        update_query = ('UPDATE books SET pages = (%s) WHERE book_id = (%s);')         # Updating SQL query
                        self.cursor.execute(update_query, (value, args))                               # executes the SQL query

                    self.connection.commit()
                    confirm_record = self.cursor.rowcount                               # confirms the number of rows updated
                    return confirm_record
            except (Exception, Error) as error:
                print(('Error while connecting to PostgreSQL:', error))
            finally:
                if self.connection:
                    self.cursor.close()        
                    self.connection.close()   
                    
                    
            
    def delete_book_record(self,args):
        try:    
                value = args
                self.connection
                querry = (f'DELETE FROM books WHERE book_id = {value};')           
                self.cursor.execute(querry)
                self.connection.commit()
                confirm_record = self.cursor.rowcount                               # confirms the number of input to database
                return confirm_record
        except (Exception, Error) as error:
            print(('Error! Could not connect to Postgres server:', error))
        finally:
            if self.connection:
                self.cursor.close()                                               
                self.connection.close()   
                    
        
if __name__ == '__main__':
    obj_of_book = Book()
    print((obj_of_book.delete_book_record(1028)))


























































# class User:
#     pass

# import psycopg2
# from psycopg2 import Error

# try:
#     # Connect to an existing database
#     connection = psycopg2.connect(user="decagon",
#                                   password="1234",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="mchenro_db")

#     # Create a cursor to perform database operations
#     cursor = connection.cursor()
#     # Print PostgreSQL details
#     print("PostgreSQL server information")
#     print(connection.get_dsn_parameters(), "\n")
#     # Executing a SQL query
#     cursor.execute("SELECT version();")
#     # Fetch result
#     record = cursor.fetchone()
#     print("You are connected to - ", record, "\n")

# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")