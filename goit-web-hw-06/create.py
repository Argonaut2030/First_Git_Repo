import logging
from psycopg2 import DatabaseError

from connect import create_connection


def create_table(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback
    finally:
        c.close()



if __name__ == '__main__':
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(120),
     email VARCHAR(120),
     password VARCHAR(120),
     age smallint
    );
    """


    try:
        with create_connection() as conn:
            if conn is not None:
                # create projects table
                create_table(conn, sql_create_users_table)
                # create tasks table
                
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)