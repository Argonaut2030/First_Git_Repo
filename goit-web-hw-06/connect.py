import psycopg2
from contextlib import contextmanager





@contextmanager
def create_connection():
    """ create a database connection to a SQLite database """
    try:
            conn = psycopg2.connect(host="localhost",database="test", user="postgres", password="420458")
            yield conn
            conn.close()
    except psycopg2.OperationalError as err:
            raise RuntimeError(f"Faild to create database connection {err}") 
            
            
 